Thespiae
========

.. contents::

Introduction
------------

Thespiae is a tool to setup Windows-based development environments; doesn't require remote repository or
prebuilt packages. It helps with routine tasks such as downloading, verification, executing/unpacking/copying/removing
and PATH environment variable manipulation. You have to specify configuration file (YAML format) and directory
to store downloaded distribution files in.

Installation
------------

Releases are available from PyPI at https://pypi.org/project/thespiae/

Usage
-----

Commands ::

    thespiae C:\config.yml C:\temp

and ::

    python -m thespiae C:\config.yml C:\temp

tell the tool to use configuration file *C:\\config.yml* and distribution file directory *C:\\temp*.

Thespiae asks you to confirm distribution download and software installation or removal, changes to current user's
*PATH* environment variable.


Configuration
-------------

Please read and accept all corresponding licenses before using this example. Check
unit tests for *conf* and *install* submodules in the source distribution to learn about config processing features,
all supported installation and removal methods. ::

    - name: vagrant
      package_url: 'https://releases.hashicorp.com/vagrant/$version/vagrant_${version}_${architecture}.msi'
      install_args:
        - 'INSTALLDIR=${install_directory}'
        - 'REBOOT=ReallySuppress'
        - 'LIMITUI=1'
      install_directory: 'C:\tools\vagrant\${version}'
      uninstall_args:
        - 'REBOOT=ReallySuppress'
        - '/qb'
      architecture: 'x86_64'
      versions:
        - version: '2.2.4'
          file_hash: '0c8cf856ed8c794db2cceef96e8cbd5f0096eeafe851b024fd0dd4b308291026'
          product_code: '{56BD544C-6113-42A4-B84C-1310DC50DFAF}'
          keep: yes
    - name: virtualbox
      installer_url: 'https://download.virtualbox.org/virtualbox/${version}/VirtualBox-${version}-${build}-Win.exe'
      install_args:
        - '--msiparams'
        - 'INSTALLDIR=${install_directory}'
        - 'VBOX_INSTALLDESKTOPSHORTCUT=0'
        - 'VBOX_INSTALLQUICKLAUNCHSHORTCUT=0'
        - 'VBOX_START=0'
        - 'LIMITUI=1'
      install_directory: 'C:\tools\virtualbox\${version}_${build}'
      uninstall_args:
        - '/qb'
      path_entries:
        - '${install_directory}'
      versions:
        - version: '6.0.4'
          build: '128413'
          file_hash: 'a7b340eaa8ad9de72373162bcbba3fc0eeed9696fa404a0e5b99c0983151a3fc'
          product_code: '{79366295-CD6A-4467-9901-4A7DFCF90F40}'
          keep: yes
    - name: git
      archive_url: 'https://github.com/git-for-windows/git/releases/download/v${version}.windows.1/Git-${version}-64-bit.tar.bz2'
      archive_format: 'bztar'
      unpack_directory: 'C:\tools\${name}\${version}'
      path_entries:
        - '${unpack_directory}\cmd'
      architecture: 'x86_64'
      versions:
        - version: '2.21.0'
          file_hash: '47f3625a78663797ae3e0dfa31c2e209461915471b0dc79b987aa2d604a8516d'
          keep: yes
    - name: gnupg
      installer_url: 'https://gnupg.org/ftp/gcrypt/binary/gnupg-w32-${version}_${build}.exe'
      install_args:
        - '/S'
        - '/D=${install_directory}'
      install_directory: 'C:\tools\${name}\${version}'
      uninstaller_path: '${install_directory}\gnupg-uninstall.exe'
      uninstall_args:
        - '/S'
      path_entries:
        - '${install_directory}\bin'
      architecture: 'x86'
      versions:
        - version: '2.2.15'
          build: '20190326'
          file_hash: '24d003adaacdbb16047a3e08fdb40b855f7ecdedc28435c767c88493260d6b25'
          keep: yes

Valid value for *file_hash* field is a *SHA-256* distribution file hash. This field can be missing; in that case, no
verification is performed for the corresponding entry.

Entries with negative or missing *keep* field value are considered for removal.


Output
------

This is output of running Thespiae with the configuration example on Windows 10. ::

    Checking software
    Download distribution for
            vagrant:2.2.4:x86_64 virtualbox:6.0.4 git:2.21.0:x86_64 gnupg:2.2.15:x86
    To install
            vagrant:2.2.4:x86_64 virtualbox:6.0.4 git:2.21.0:x86_64 gnupg:2.2.15:x86
    Continue? [y/N]:y
    Downloading
    vagrant:2.2.4:x86_64: 100%|#########################################################| 240M/240M [01:12<00:00, 3.30MB/s]
        virtualbox:6.0.4: 100%|#########################################################| 220M/220M [01:12<00:00, 3.02MB/s]
       git:2.21.0:x86_64: 100%|#########################################################| 100M/100M [01:12<00:00, 1.38MB/s]
        gnupg:2.2.15:x86: 100%|#######################################################| 4.18M/4.18M [01:12<00:00, 57.4kB/s]
    Installing software
    [1/4] installing vagrant:2.2.4:x86_64
    vagrant:2.2.4:x86_64 installed
    [2/4] installing virtualbox:6.0.4
    virtualbox:6.0.4 installed
    [3/4] installing git:2.21.0:x86_64
    git:2.21.0:x86_64 installed
    [4/4] installing gnupg:2.2.15:x86
    gnupg:2.2.15:x86 installed
    Checking user PATH
    Current user PATH
            %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
    Updated user PATH
            %USERPROFILE%\AppData\Local\Microsoft\WindowsApps;C:\tools\virtualbox\6.0.4_128413;C:\tools\git\2.21.0\cmd;C:\tools\gnupg\2.2.15
    Continue? [y/N]:y
    User PATH updated


License
-------

Thespiae is released under version 2.0 of the `Apache License`_.

.. _Apache License: http://www.apache.org/licenses/LICENSE-2.0