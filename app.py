#                     __                      ______              
# .-----.-----.--.--.|  |--.-----.----.-----.|      |.-----.-----.
# |  _  |__ --|  |  ||  _  |  _  |   _|  _  ||  --  ||     |  -__|
# |   __|_____|___  ||_____|_____|__| |___  ||______||__|__|_____|#4689
# |__|        |_____|                 |_____| app.py
# 
# Licensed under the terms of the LICENSE file included in this repo.
# Created On   : We, September 6th 2023, 10:39:35
# Last Modified: Th, September 7th 2023, 01:59:53

import os
import shutil
import xml.etree.ElementTree as ET

# default_path_config_dir     = 'K:\AosService\WebRoot'
default_path_config_dir     = '.'
default_name_config_file    = 'web.config'
default_path_config_file    = os.path.join(default_path_config_dir, default_name_config_file)
default_ext_backup_file     = '.back'
default_path_backup_file    = os.path.join(default_path_config_dir, f"{default_name_config_file}{default_ext_backup_file}")
default_properties_dict     = {"DataAccess.DbServer": "localhost",
                                "DataAccess.Database": "AxDB",
                                "DataAccess.SqlUser": "user",
                                "DataAccess.SqlPwd": "pass"}

def existsFile(_path_to_file)-> bool:
    return True if os.path.exists(_path_to_file) else False

def createBackup(_path_to_file= ''):
    try:
        if(existsFile(default_path_config_file)):
            print(f"FOUND: {default_path_config_file}")
            print("Creating backup...")
            shutil.copy(default_path_config_file, default_path_backup_file)
            print(f"Backup created!\nPath: {default_path_backup_file}")

    except:
        print("There was a problem creating the backup file.")

def restoreBackup():
    try:
        if(existsFile(default_path_backup_file)):
            print(f"FOUND: {default_path_backup_file}")
            print("Restoring backup...")
            shutil.copy(default_path_backup_file, default_path_config_file)
            print(f"Backup restored!\nPath: {default_path_config_file}")

    except:
        print("There was a problem restoring the backup file.")

def openAndWriteChanges(_properties)-> bool:
    isOpOk = False

    try:
        config_tree = ET.parse(default_path_config_file)
        config_root = config_tree.getroot()

        for category in config_root.findall("appSettings"):
            for line in category:
                
                lineKey     = line.attrib['key']
                lineValue     = line.attrib['value']

                if(lineKey in _properties.keys()):
                    
                    for key, value in _properties.items():
                        if(lineKey == key):
                            line.set('value', _properties.get(lineKey))
                            print(f"[{lineKey}] - {lineValue} -> {line.attrib['value']}")

        config_tree.write(default_path_config_file)

        isOpOk = True

    except:
        print("Something went wrong while updating values inside config file")

        isOpOk = False

    finally:
        return isOpOk

def setPropertyField(_fieldName, _fieldValue)-> dict:
    default_properties_dict[_fieldName] = _fieldValue
    return default_properties_dict