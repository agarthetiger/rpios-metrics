# rpios-metrics

Ansible Role to install a python daemon process which will provide an http endpoint for exposing system metrics.

This role exists because I'm building a Raspberry Pi cluster with custom case which will have a single PWM fan. One Pi in the cluster needs to get the cpu temperature for all the cluster hosts in order to control the fan speed appropriately. I've decided that an unsecured endpoint which exposes the onboard temp as measured by vcgen is adequate for my purposes.

# Requirements

Python3 must be installed.

# Role Variables

| Variable | Default value | Description |
|----------|---------------|-------------|
| daemon_install_path | /opt/metrics_daemon | Folder to install the python web service code into. |
| daemon_user | pi | User to run the system service as. |
| daemon_group | pi | Group to run the system service as. |
| daemon_port | '5000' | Port to expose the web service on. |
| daemon_service_path | /etc/systemd/system | Folder to install the service template into. |

# Dependencies

None.

# Example Playbook

```yaml
- hosts: rpicluster
  roles:
    - rpios-metrics
```

# License

MIT

# Author Information

@agarthetiger
