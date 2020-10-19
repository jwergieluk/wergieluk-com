---
title: "Meet your new Signal messenger contact: systemd"
date: 2020-10-03
draft: true
markup: "markdown"
katex: true
tags:
    - linux
---

* https://opensource.com/article/20/4/systemd
* Systemd user services: https://www.unixsysadmin.com/systemd-user-services/
* Send an email on service failure: https://northernlightlabs.se/2014-07-05/systemd-status-mail-on-unit-failure.html

[Signal](https://signal.org/en/) is an open-source messenger supporting common mobile platforms and 
sporting a strong cryptography support. Although, the functionality is on par with Whatsapp, not many people seem 
to be using Signal.  

On the machine I use to write this post, `journalctl` lists over 200 log entries made today. Some of them quite funny 
(edited for brevity):

    syncthing: INFO: Connected to myself ... - should not happen

Would it be possible to have systemd as a Signal contact and all those "news" directly? Yes!  

There is a signal client for linux. Let's download it first: https://github.com/AsamK/signal-cli

Setup is described here: https://github.com/AsamK/signal-cli/wiki/Quickstart

Use the provided compiled and ready-to-use binaries. These require a recent version of Java run-time to run.
On my arch linux I had to install `jdk-openjdk` packages and set the default Java version using the `archlinux-java` 
command. More info here: https://wiki.archlinux.org/index.php/java

Uncompressed signal tar should contain a command-line client ready to use

    $ signal-cli-0.6.10/bin/signal-cli --help 
    usage: signal-cli [-h] [-v] [--config CONFIG] [-u USERNAME | --dbus | --dbus-system]

    export PHONE_NUMBER="+00000000"
    signal-cli-0.6.10/bin/signal-cli -u $PHONE_NUMBER register
 

    signal-cli -u USERNAME verify CODE
    signal-cli-0.6.10/bin/signal-cli -u $PHONE_NUMBER verify 872-684

    signal -u $SIGNAL_USER send -m 'First message from eilenberg' $PHONE_NUMBER



    $ signal -u $SIGNAL_USER receive 
    Envelope from: .. (device: 1)
    Timestamp: 1601727663176 (2020-10-03T12:21:03.176Z)
    Got receipt.
    
    Envelope from: “null” .. (device: 1)
    Timestamp: 1601728021727 (2020-10-03T12:27:01.727Z)
    Sender: “null” .. (device: 1)
    Message timestamp: 1601728021727 (2020-10-03T12:27:01.727Z)
    Profile key update, key length:32
    
    Envelope from: “null” .. (device: 1)
    Timestamp: 1601728021734 (2020-10-03T12:27:01.734Z)
    Sender: “null” .. (device: 1)
    Received a receipt message
     - When: 1601728021734 (2020-10-03T12:27:01.734Z)
     - Is read receipt
     - Timestamps:
        1601727663176 (2020-10-03T12:21:03.176Z)
    
    Envelope from: “null” .. (device: 1)
    Timestamp: 1601728617450 (2020-10-03T12:36:57.450Z)
    Sender: “null” .. (device: 1)
    Message timestamp: 1601728617450 (2020-10-03T12:36:57.450Z)
    Body: Hey dude 😁😎!
    Profile key update, key length:32

Start signal-cli as a D-Bus service and send message using that service.

    $ signal -u $SIGNAL_USER daemon 
    Envelope from: unknown source
    Timestamp: 1601732907218 (2020-10-03T13:48:27.218Z)
    Sent by unidentified/sealed sender
    Sender: “null” .. (device: 1)
    Received a receipt message
     - When: 1601732907218 (2020-10-03T13:48:27.218Z)
     - Is delivery receipt
     - Timestamps:
        1601732644496 (2020-10-03T13:44:04.496Z)
    
    Envelope from: unknown source
    Timestamp: 1601732923584 (2020-10-03T13:48:43.584Z)
    Sent by unidentified/sealed sender
    Sender: “null” .. (device: 1)
    Received a receipt message
     - When: 1601732923584 (2020-10-03T13:48:43.584Z)
     - Is read receipt
     - Timestamps:
        1601732644496 (2020-10-03T13:44:04.496Z)

When sending over D-Bus, where is no need to specify the sender (just the recipient).

    $ export PHONE_NUMBER_JULIAN='...'
    $ signal --dbus send -m "Message send using D-Bus" $PHONE_NUMBER_JULIAN


## Plan

* Write a system service for the D-Bus daemon (with separate user)
* Write a bash wrapper script for sending messages. (To put the recipient name to a config file)
* 


