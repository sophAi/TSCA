#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# ==============================================================
# Copyright(c) 2016-, Po-Jen Hsu (clusterga@gmail.com)
# See the README file in the top-level directory for license.
# ==============================================================
# Creation Time : 20160627 10:46:26
# ==============================================================
from importlib import util
from json import loads
from os import system, walk
from os.path import abspath, expanduser, isdir
from sys import argv, path, exit


preference_file = None
prefernce = None
def_tmp_path = abspath(expanduser("~/.cache/enigma"))
if len(argv) == 2 and argv[1] != "-h":
    preference_file = argv[1]
else:
    for arg_id, arg in enumerate(argv):
        if "--preference=" in arg:
            preference_file = abspath(expanduser(arg.split("=")[-1]))
        elif "-p" in arg:
            preference_file = abspath(expanduser(argv[arg_id + 1]))
if preference_file:
    with open(preference_file, "r") as pref_obj:
        preference = loads(pref_obj.read())
try:
    key_url, key_str = preference["key"]
    key, alg = key_str.split(".")
except:
    print("Using default environment...")
    search_key_path = next(walk(def_tmp_path))[1]
    if search_key_path:
        path.insert(1, "{}/{}".format(def_tmp_path, search_key_path[0]))
else:
    if "tmp_path" in preference and preference["tmp_path"]:
        tmp_path = abspath(expanduser(preference["tmp_path"]))
    else:
        tmp_path = def_tmp_path
    key_path = "{}/{}_{}".format(tmp_path, key, util.MAGIC_NUMBER.hex())
    if not isdir(key_path):
        print("Initializing...")
        from hashlib import new
        from importlib import machinery, _bootstrap_external
        from sqlite3 import connect
        key_file_path = "{}/{}".format(key_path, key_str)
        system("mkdir -p {}".format(key_path))
        system("wget -q --no-check-certificate '{}' -O {}"
               .format(key_url,
                       key_file_path))
        with open(key_file_path, "rb") as key_obj:
            read_chunk = "reading"
            hash_obj = new(alg)
            while read_chunk:
                read_chunk = key_obj.read(4092)
                start = 0
                while start < 4092:
                    hash_obj.update(read_chunk[start:start + 1024])
                    start += 1024
        if hash_obj.hexdigest() != key:
            print("Error! Invalid key.")
            exit(1)
        key_file = connect(key_file_path)
        key_cur = key_file.cursor()
        table_ext = "py"
        table_list = [
            table_ext+"_name",
            table_ext+"_mtime",
            table_ext+"_content",
        ]
        table_dict = {}
        for table in table_list:
            table_dict[table] = []
            key_cur.execute(
                "SELECT {} FROM {}".format(table[len(table_ext)+1:], table)
            )
            for row in key_cur.fetchall():
                table_dict[table].append(row[0])
        key_file.close()
        for I0, py_code in enumerate(table_dict[table_ext+"_content"]):
            try:
                py_name = table_dict[table_ext+"_name"][I0].split(".")[0]
                loader_obj = machinery.SourceFileLoader(
                    "<py_compile>",
                    py_name,
                )
                code_obj = loader_obj.source_to_code(
                    py_code,
                    py_name,
                    _optimize=-1,
                )
                bytecode = _bootstrap_external._code_to_bytecode(
                    code_obj,
                    mtime=table_dict[table_ext+"_mtime"][I0],
                    source_size=len(py_code),
                )
            except:
                print("Somthing wrong in {}".format(py_name))
            else:
                _bootstrap_external._write_atomic(
                    "{}/{}.pyc".format(key_path, py_name),
                    bytecode,
                    33188,
                )
        system("rm -rf {}".format(key_file_path))
    path.insert(1, key_path)
print("Starting...")
from cli_argv_tools import cli_argv
from enigma import enigma
enigma(pref=cli_argv(argv))
