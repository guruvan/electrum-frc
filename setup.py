#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('util', 'lib/util.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum-frc requires Python version >= 2.7.0...")



if (len(sys.argv) > 1) and (sys.argv[1] == "install"): 
    # or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files = []
    usr_share = util.usr_share_dir()
    if not os.access(usr_share, os.W_OK):
        try:
            os.mkdir(usr_share)
        except:
            sys.exit("Error: cannot write to %s.\nIf you do not have root permissions, you may install Electrum-frc in a virtualenv.\nAlso, please note that you can run Electrum-frc without installing it on your system."%usr_share)

    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-frc.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-frc.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))


    appdata_dir = os.path.join(usr_share, "electrum-frc")
    data_files += [
        (appdata_dir, ["data/README"]),
        (os.path.join(appdata_dir, "cleanlook"), [
            "data/cleanlook/name.cfg",
            "data/cleanlook/style.css"
        ]),
        (os.path.join(appdata_dir, "sahara"), [
            "data/sahara/name.cfg",
            "data/sahara/style.css"
        ]),
        (os.path.join(appdata_dir, "dark"), [
            "data/dark/name.cfg",
            "data/dark/style.css"
        ])
    ]

    for lang in os.listdir('data/wordlist'):
        data_files.append((os.path.join(appdata_dir, 'wordlist'), ['data/wordlist/%s' % lang]))
else:
    data_files = []

setup(
    name="Electrum-frc",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes==0.1a1',
        'ecdsa==0.13',
        'pbkdf2==1.3',
        'requests==2.5.1',
        'pyasn1-modules==0.0.5',
        'pyasn1==0.1.7',
        'qrcode==5.1',
        'SocksiPy-branch==1.01',
        'protobuf==2.6.1',
        'tlslite==0.4.8'
    ],
    package_dir={
        'electrum_frc': 'lib',
        'electrum_frc_gui': 'gui',
        'electrum_frc_plugins': 'plugins',
    },
    scripts=['electrum-frc'],
    data_files=data_files,
    py_modules=[
        'electrum_frc.account',
        'electrum_frc.bitcoin',
        'electrum_frc.blockchain',
        'electrum_frc.bmp',
        'electrum_frc.commands',
        'electrum_frc.daemon',
        'electrum_frc.i18n',
        'electrum_frc.interface',
        'electrum_frc.mnemonic',
        'electrum_frc.msqr',
        'electrum_frc.network',
        'electrum_frc.network_proxy',
        'electrum_frc.old_mnemonic',
        'electrum_frc.paymentrequest',
        'electrum_frc.paymentrequest_pb2',
        'electrum_frc.plugins',
        'electrum_frc.qrscanner',
        'electrum_frc.simple_config',
        'electrum_frc.synchronizer',
        'electrum_frc.transaction',
        'electrum_frc.util',
        'electrum_frc.verifier',
        'electrum_frc.version',
        'electrum_frc.wallet',
        'electrum_frc.x509',
        'electrum_frc_gui.gtk',
        'electrum_frc_gui.qt.__init__',
        'electrum_frc_gui.qt.amountedit',
        'electrum_frc_gui.qt.console',
        'electrum_frc_gui.qt.history_widget',
        'electrum_frc_gui.qt.icons_rc',
        'electrum_frc_gui.qt.installwizard',
        'electrum_frc_gui.qt.lite_window',
        'electrum_frc_gui.qt.main_window',
        'electrum_frc_gui.qt.network_dialog',
        'electrum_frc_gui.qt.password_dialog',
        'electrum_frc_gui.qt.paytoedit',
        'electrum_frc_gui.qt.qrcodewidget',
        'electrum_frc_gui.qt.qrtextedit',
        'electrum_frc_gui.qt.qrwindow',
        'electrum_frc_gui.qt.receiving_widget',
        'electrum_frc_gui.qt.seed_dialog',
        'electrum_frc_gui.qt.transaction_dialog',
        'electrum_frc_gui.qt.util',
        'electrum_frc_gui.qt.version_getter',
        'electrum_frc_gui.stdio',
        'electrum_frc_gui.text',
        'electrum_frc_plugins.btchipwallet',
        'electrum_frc_plugins.coinbase_buyback',
        'electrum_frc_plugins.cosigner_pool',
        'electrum_frc_plugins.exchange_rate',
        'electrum_frc_plugins.greenaddress_instant',
        'electrum_frc_plugins.labels',
        'electrum_frc_plugins.trezor',
        'electrum_frc_plugins.virtualkeyboard',
        'electrum_frc_plugins.plot',

    ],
    description="Lightweight Freicoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU GPLv3",
    url="https://electrum.org",
    long_description="""Lightweight Freicoin Wallet"""
)
