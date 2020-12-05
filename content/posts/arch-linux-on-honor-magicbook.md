---
title: "Arch Linux on Honor Magicbook"
slug: magicbook
date: 2020-12-02T21:11:32+01:00
modified: 2020-12-05
draft: false
---

Last week I bought a Honor MagicBook 14 laptop. This blog post documents
setting up an Arch Linux system on it. 

I am not quite done with it yet. Here is my to-do list: 

* Fix the DPI setting for Xorg
* Power-management: Test sleep on lid-close.
* i3
    * Use the Windows key for meta
    * dmenu has weird looking fonts
    * status line is not nice
* Setup up hot-keys. Especialy ones for
    * setting the screen brightness, 
    * volume, and
    * microphone muting/unmuting
* Test webcam. 
* Test sound.
* Install: pycharm

# Hardware information

Diagnostic tools output: [lspci](/magicbook/lspci.txt) [lscpu](/magicbook/lscpu.txt)

{{< figure src="/magicbook/bios.jpg" title="BIOS screenshot" >}}

# Base system installation

Get an archlinux image (not the bootstrap image) from here https://www.archlinux.org/download/ 

Calculate the checksum.

    $ sha1sum archlinux-2020.12.01-x86_64.iso 
    aea95a15c9f034d10e665247cfe782bccb5b306e  archlinux-2020.12.01-x86_64.iso

Copy image on a USB stick. This is surprisingly simple on a Linux system (be
careful to specify the right device).

    # cat archlinux-2020.12.01-x86_64.iso > /dev/sdg

Other methods are described here: 
https://wiki.archlinux.org/index.php/USB_flash_installation_medium#Using_basic_command_line_utilities

Enter BIOS by pressing `F1`, `F2`, or `Del` (I pressed all of them, don't know
which one worked). Change settings to booting from USB device. Disable secure
boot. Restart.

https://wiki.archlinux.org/index.php/Installation_guide

    loadkeys de-latin1

No idea why verifying the boot mode is important. I apparently booted in the UEFI mode.
https://wiki.archlinux.org/index.php/Arch_boot_process 

    ls /sys/firmware/efi/efivars

## Wifi connection setup

    iwctl

Connect by follwing this: https://wiki.archlinux.org/index.php/Iwd#Connect_to_a_network

## Saying goodbye to Windows

{{< figure src="/magicbook/original-partitioning.jpg" title="Original partition table" >}}

Get rid of every partition except EFI one.

    fdisk -l

Repartition and create new file systems.

Mount root and swap, and `pacstrap` with some additional packages from 
https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/configs/releng/packages.x86_64

## Keyboard map and locale

Set and generate locale. Save config to `/etc/locale.conf`

Set keyboard layout in `/ect/vconsole.conf`

    KEYMAP=us

Other layouts are listed here: 
    
    ls /usr/share/kbd/keymaps/**/*.map.gz

## Boot loader installation

Install `grub` and `efibootmgr` packages. Follow https://wiki.archlinux.org/index.php/GRUB for UEFI systems. 

# Post-installation

https://wiki.archlinux.org/index.php/General_recommendations

Add a user.

    useradd -m -G rfkill,wheel julian

## Networking

Enable `iwd.service`. Connect to a wireless network using `iwctl`. Enable DHCP
feature of `iwd` in the config file `/etc/iwd/main.conf`:

    [General]
    EnableNetworkConfiguration=true

    [Network]
    NameResolvingService=systemd

Finally:

    systemctl enable --now systemd-resolved.service

## Xorg

Graphic card rriver package: `amdgpu` https://wiki.archlinux.org/index.php/AMDGPU 

Display manager: None -- just use `.xinitrc`

Window manager package: `i3-wm`

## i3 window manager

`dmenu` a had weird-looking fonts setting (huge distance between letter).
Following solution posted at https://www.reddit.com/r/i3wm/comments/fxz4hj/help_the_letter_spacing_in_my_dmenu_bar_is_weird/


## Terminal emulator

Decided to try `kitty`, after having some trouble with fonts in urxtv. 

### Kitty terminal emulator

Color themes can be cloned right into the config directory

    git clone --depth 1 git@github.com:dexpota/kitty-themes.git ~/.config/kitty/kitty-themes

## Vim configuration

Zenburn colors. Do `git clone https://github.com/jnurmine/Zenburn.git` and copy the
`colors` directory to `~/.vim/colors`. 

Here is my [.vimrc](/config/vimrc) file.

## ssh agents

Generate ssh keys (for Github, Gitlab etc.) using

    ssh-keygen -t ed25519 -C 'julian@wergieluk.com'

Append `AddKeysToAgent yes` to `.ssh/config` to have the new keys managed by the `ssh-agent` automatically. I decided to start the ssh-agent using a user systemd service. Copied the service file from https://wiki.archlinux.org/index.php/SSH_keys#Start_ssh-agent_with_systemd_user

Testing the connection:

    ssh -T git@github.com





