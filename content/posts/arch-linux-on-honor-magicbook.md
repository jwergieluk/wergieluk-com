---
title: "Arch Linux on Honor Magicbook"
date: 2020-12-02T21:11:32+01:00
draft: true
---

Installation notes.


Get an archlinux image (not the bootstrap image) from here https://www.archlinux.org/download/ 

Calculate the checksum.

    $ sha1sum archlinux-2020.12.01-x86_64.iso 
    aea95a15c9f034d10e665247cfe782bccb5b306e  archlinux-2020.12.01-x86_64.iso

Copy image on a USB stick. This is surprisingly simple on a Linux system (Be
careful to specify the right device).

    # cat archlinux-2020.12.01-x86_64.iso > /dev/sdg

Other methods are described here: 
https://wiki.archlinux.org/index.php/USB_flash_installation_medium#Using_basic_command_line_utilities

BIOS with F1, F2, or Del (I pressed all of them, don't know which one worked). Change settings to booting from USB device. Disable secure boot. Restart.

https://wiki.archlinux.org/index.php/Installation_guide


    loadkeys de-latin1


No idea why verifying the boot mode is important. I apparently booted in the UEFI mode.
https://wiki.archlinux.org/index.php/Arch_boot_process 

    ls /sys/firmware/efi/efivars

# Setup wifi connection

    iwctl

Connect by follwing this: https://wiki.archlinux.org/index.php/Iwd#Connect_to_a_network

# Say goodbye to Windows

Get rid of every partition except EFI one.

    fdisk -l

Repartition and create new file systems.

Mount root and swap and `pacstrap` with some additional packages from 
https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/configs/releng/packages.x86_64

Set and generate locale. Save config to `/etc/locale.conf`

Set keyboard layout in `/ect/vconsole.conf`

    KEYMAP=us

Other layouts are listed here: 
    
    ls /usr/share/kbd/keymaps/**/*.map.gz

Install `grub` and `efibootmgr` packages. Follow https://wiki.archlinux.org/index.php/GRUB for UEFI systems. 

# Post-installation

https://wiki.archlinux.org/index.php/General_recommendations

Add a user.

    useradd -m -G rfkill,wheel julian

## Networking

Enable `iwd.service`. Connect to a wireless network using `iwctl`. Enable DHCP feature of `iwd`.

    systemctl enable --now systemd-resolved.service

## Xorg

Driver package: `amdgpu`.  https://wiki.archlinux.org/index.php/AMDGPU 
Display manager: `lightdm`
Window manager package: `i3-wm`


