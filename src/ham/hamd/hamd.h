// Host Account Management
#ifndef HAMD_H
#define HAMD_H

#include <dbus-c++/dbus.h>          // DBus::Connection
#include <glib.h>                   // gint, gpointer
#include "timer.h"                  // gtimer_c
#include "../shared/dbus-address.h" // DBUS_BUS_NAME_BASE

#include "../shared/org.SONiC.HostAccountManagement.dbus-adaptor.h"

class hamd_config_c
{
public:
    hamd_config_c(int argc, char **argv);

    /**
     * @brief Read configuration and update hamd_config_c object
     */
    void reload();

    uid_t uid_fit_into_range(uint64_t hash) const
    {
        return (uid_t)((hash % sac_uid_range_m) + sac_uid_min_m);
    }

    /**
     * @brief return the shell program to assign to new users.
     */
    const std::string & shell() const {return shell_m;}

    std::string to_string() const;
    bool        is_tron()   const { return tron_m; }

private:
    // PLEASE UPDATE etc/sonic/hamd/config
    // WHEN MAKING CHANGES TO DEFAULTS
    static const  gint  poll_period_sec_default_m = 30;
    static const  gint  sac_uid_min_default_m     = 5000;  // System-Assigned IDs will be in the
    static const  gint  sac_uid_max_default_m     = 59999; // range [sac_uid_min_m..sac_uid_max_m]
    static const  bool  tron_default_m            = false;
    const gchar       * conf_file_default_pm      = "/etc/sonic/hamd/config";
    std::string         certgen_default_m         = "/usr/bin/certgen";
    //std::string         shell_default_m           = "/usr/bin/sonic-cli";
    //std::string         shell_default_m           = ""; // empty string -> let linux assign default shell (as per /etc/default/useradd)
    std::string         shell_default_m           = "/bin/bash";

public:
    bool                tron_m                    = tron_default_m;
    gint                poll_period_sec_m         = poll_period_sec_default_m;

    gint                sac_uid_min_m             = sac_uid_min_default_m;  // System-Assigned IDs will be in the
    gint                sac_uid_max_m             = sac_uid_max_default_m;  // range [sac_uid_min_m..sac_uid_max_m]

    std::string         certgen_m                 = certgen_default_m;

private:
    const gchar       * conf_file_pm              = conf_file_default_pm;
    std::string         shell_m                   = shell_default_m;
    gint                sac_uid_range_m           = 1 + (sac_uid_max_m - sac_uid_min_m);
};

std::ostream & operator<<(std::ostream  & stream_r, const hamd_config_c  & obj_r);



class hamd_c : public DBus::ObjectAdaptor,
               public DBus::IntrospectableAdaptor,
               public ham::accounts_adaptor,
               public ham::name_service_adaptor,
               public ham::debug_adaptor
{
public:
    hamd_c(hamd_config_c & config_r, DBus::Connection  & conn_r);
    virtual ~hamd_c() {}

    // DBus "accounts" interface
    virtual ::DBus::Struct< bool, std::string > useradd(const std::string& login, const std::vector< std::string >& roles, const std::string& hashed_pw);
    virtual ::DBus::Struct< bool, std::string > userdel(const std::string& login);
    virtual ::DBus::Struct< bool, std::string > passwd(const std::string& login, const std::string& hashed_pw);
    virtual ::DBus::Struct< bool, std::string > set_roles(const std::string& login, const std::vector< std::string >& roles);
    virtual ::DBus::Struct< bool, std::string > groupadd(const std::string& group);
    virtual ::DBus::Struct< bool, std::string > groupdel(const std::string& group);

    // DBus "nss" interface
    virtual ::DBus::Struct< bool, std::string, std::string, uint32_t, uint32_t, std::string, std::string, std::string > getpwnam(const std::string& name);
    virtual ::DBus::Struct< bool, std::string, std::string, uint32_t, uint32_t, std::string, std::string, std::string > getpwuid(const uint32_t& uid);
    virtual std::string getpwcontents();
    virtual ::DBus::Struct< bool, std::string, std::string, uint32_t, std::vector< std::string > > getgrnam(const std::string& name);
    virtual ::DBus::Struct< bool, std::string, std::string, uint32_t, std::vector< std::string > > getgrgid(const uint32_t& gid);
    virtual std::string getgrcontents();
    virtual ::DBus::Struct< bool, std::string, std::string, int32_t, int32_t, int32_t, int32_t, int32_t, int32_t, uint32_t > getspnam(const std::string& name);


    // DBus "sac" interface
    virtual std::string add_unconfirmed_user(const std::string & login, const uint32_t & pid);
    virtual std::string user_confirm(const std::string & login, const std::vector<std::string> & roles);

    // DBus "debug" interface
    virtual std::string  tron();
    virtual std::string  troff();
    virtual std::string  show();

    bool                 is_tron() const { return config_rm.tron_m; }
    virtual void         cleanup();
    void                 reload();
    void                 apply_config();

private:
    hamd_config_c      & config_rm;
    gtimer_c             poll_timer_m;
    static bool          on_poll_timeout(gpointer user_data_p); // This callback functions must follow GSourceFunc signature.
    void                 rm_unconfirmed_users() const;
    std::string          certgen(const std::string  & login) const;
};

#endif /* HAMD_H */
