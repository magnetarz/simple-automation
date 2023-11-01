edge-firewall:
    connections:
      cli:
        ip: 10.10.20.171
        protocol: telnet
    credentials:
      default:
        password: cisco
        username: '%ASK{}'
      enable:
        password: '%ASK{}'
    os: asa
    type: asa

  edge-sw01:
    connections:
      cli:
        ip: 10.10.20.172
        protocol: ssh
    credentials:
      default:
        password: cisco
        username: cisco
      enable:
        password: '%ASK{}'
    os: iosxe
    type: iosxe