---
title: "Installing Arch Linux on Honor Magicbook"
slug: magicbook
date: 2020-12-02T21:11:32+01:00
modified: 2020-12-05
draft: false
---

Last week I bought a Honor MagicBook 14 laptop. This blog post documents
setting up an Arch Linux system on this machine. 

# Hardware information

Tech specs for the Honor MagicBook 14 with 16GB RAM and a 512GB SDD:
https://www.hihonor.com/germany/product/honor-magicbook-14#18149188113454

* CPU: AMD Ryzen ™ 5 3500U Prozessor
* Graphic card: Radeon™ Vega 8 Graphics
* Display: 14", 1920 x 1080, 157 DPI

Outputs produced by common diagnostic tools: [lspci](/magicbook/lspci.txt)
[lscpu](/magicbook/lscpu.txt) [lsusb](/magicbook/lsusb.txt)

{{< figure src="/magicbook/bios.jpg" title="BIOS screenshot" >}}

# Base system installation

Get an archlinux image (not the bootstrap image) from here https://www.archlinux.org/download/ 

Calculate the checksum.

    $ sha1sum archlinux-2020.12.01-x86_64.iso 
    aea95a15c9f034d10e665247cfe782bccb5b306e  archlinux-2020.12.01-x86_64.iso

Copy image on a USB drive. This is surprisingly simple on a Linux system (be
careful to specify the right device).

    # cat archlinux-2020.12.01-x86_64.iso > /dev/sdg

Other methods are described here: 
https://wiki.archlinux.org/index.php/USB_flash_installation_medium#Using_basic_command_line_utilities

After we are done, the USB drive can be restored with

    wipefs --all /dev/sdX
    fdisk /dev/sdX 
    # create a primary partition with code 'b'
    mkfs.vfat /dev/sdX1 

Enter the BIOS by pressing `F1`, `F2`, or `Del` (I pressed all these keys, don't know
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

Get rid of every partition except the EFI one.

    fdisk -l

Repartition and create new file systems.

    Device            Start        End   Sectors   Size Type
    /dev/nvme0n1p1     2048     206847    204800   100M EFI System
    /dev/nvme0n1p2   206848   33761279  33554432    16G Linux swap
    /dev/nvme0n1p3 33761280 1000215182 966453903 460.8G Linux root (x86-64)

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

# Configuration

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

Graphic card driver package: `amdgpu` https://wiki.archlinux.org/index.php/AMDGPU 

Display manager: None -- just use `.xinitrc` and `startx`

Window manager package: `i3-wm`

### Setting the right DPI

According to the tech spec, the DPI of the display is 157. Xorg doesn't detect
this automatically as can be seen from the `xpdyinfo` output

    screen #0:
      dimensions:    1920x1080 pixels (508x285 millimeters)
      resolution:    96x96 dots per inch

There are many ways to set a DPI value. For example, using `.xinitrc`, we can do

    xrandr --dpi 144
    exec i3

## i3 window manager

Volume and mute keys work out-of-the-box. This is not the case for for screen
backlight hotkeys. See the "Power management" section.

`dmenu` had a weird-looking fonts setting (huge distances between letters).
Following solution posted at https://www.reddit.com/r/i3wm/comments/fxz4hj/help_the_letter_spacing_in_my_dmenu_bar_is_weird/

## Terminal emulator

Decided to try `kitty`, after having some trouble with fonts in urxtv. 

### Kitty terminal emulator

Color themes can be cloned right into the config directory

    git clone --depth 1 git@github.com:dexpota/kitty-themes.git ~/.config/kitty/kitty-themes

Also, to convince `i3-sensible-terminal` to use `kitty` per default we need

    export TERMINAL=kitty

## Vim configuration

Zenburn colors are not shipped as a part on any standard package. Do `git clone
https://github.com/jnurmine/Zenburn.git` and copy the `colors` directory to
`~/.vim/colors` to get the scheme definition. 

Here is my [.vimrc](/config/vimrc) file.

## ssh agents

Generate ssh keys (for Github, Gitlab etc.) using

    ssh-keygen -t ed25519 -C 'julian@wergieluk.com'

Append `AddKeysToAgent yes` to `.ssh/config` to have the new keys managed by
the `ssh-agent` automatically. I decided to start the ssh-agent using a user
systemd service. Copied the service file from
https://wiki.archlinux.org/index.php/SSH_keys#Start_ssh-agent_with_systemd_user

Testing the connection:

    ssh -T git@github.com

## Power management

Is there a way to measure whether these settings bring anything?

* Add the line `options snd_hda_intel power_save=1` to
  `/etc/modprobe.d/audio-powersave.conf` to susspend sound card if not used.

Another recommended way to save power, is to blacklist modprobe modules of
unused devices. For that I created a file `/etc/modprobe.d/blacklist.conf` with
a list of modules, and included that file in the `FILES` array of
`/etc/mkinitcpio.conf`:

    FILES=(/etc/modprobe.d/blacklist.conf)

Blacklisted modules:

* `ccp` for "[AMD] Family 17h (Models 10h-1fh) Platform Security Processor"
* `btusb` for bluetooth.

### Screen brightness

`xev` events when pressing the brightness-up and brightness-down keys:

    KeyRelease event, serial 35, synthetic NO, window 0x2200001,
        root 0x6ab, subw 0x0, time 49258531, (-1,720), root:(963,742),
        state 0x0, keycode 232 (keysym 0x1008ff03, XF86MonBrightnessDown), same_screen YES,
        XLookupString gives 0 bytes: 
        XFilterEvent returns: False

    KeyPress event, serial 35, synthetic NO, window 0x2200001,
        root 0x6ab, subw 0x0, time 49263961, (-1,720), root:(963,742),
        state 0x0, keycode 233 (keysym 0x1008ff02, XF86MonBrightnessUp), same_screen YES,
        XLookupString gives 0 bytes: 
        XmbLookupString gives 0 bytes: 
        XFilterEvent returns: False

Set user permissions to modify screen brightness:

    gpasswd -a julian video

With these permissions in place, the backlight intensity can be set using

    $ echo 100 > /sys/class/backlight/amdgpu_bl0/brightness

or a specialized utility listed on
https://wiki.archlinux.org/index.php/backlight#Backlight_utilities 

I ended up using `brightnessctl` which is written in C and has no dependencies.
Wiring the `brightnessctl` invocations to keysyms listed above can be done in
the i3 config file (note the `5%-` notation).

    bindsym XF86MonBrightnessDown exec --no-startup-id brightnessctl set 5%-
    bindsym XF86MonBrightnessUp exec --no-startup-id brightnessctl set +5%

## Webcam

Works.

## Hardware accelarated video decoding

https://wiki.archlinux.org/index.php/Hardware_video_acceleration

https://wiki.archlinux.org/index.php/Firefox#Hardware_video_acceleration

## Misc

Sound works out-of-the-box after installing `pulseaudio` and `pulseaudio-alsa`.

# Conclusion

Setting Arch Linux with a non-standard window manager like i3 clearly requires
some effort and knowledge. I didn't hit any major roadblocks like missing
hardware drivers. Most of necessary steps are clearly described on the Arch
wiki. I learned some interesting details about Xorg while working on this
installation.

<!-- vim: set syntax=markdown: set spelllang=en_us: set spell: -->
