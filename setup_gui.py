#!/usr/bin/env python3
"""
Script para compilar o Gerenciador de Spam do Gmail com interface gráfica.

Este script usa cx_Freeze para criar um executável autônomo.
"""

import sys
import os
from cx_Freeze import setup, Executable

# Diretório base
base_dir = os.path.abspath(os.path.dirname(__file__))

# Arquivos a incluir
include_files = [
    "README_SPAM_DELETION.md",
    "configuracao_exclusao_automatica_spam.md",
    "icones"
]

# Pacotes a incluir
packages = [
    "tkinter",
    "sqlite3",
    "cryptography",
    "logging",
    "threading",
    "queue",
    "imaplib",
    "email",
    "datetime",
    "base64",
    "hashlib"
]

# Módulos a incluir
includes = [
    "credential_prompt",
    "credentials_manager",
    "delete_spam_emails",
    "check_spam_count",
    "verificar_spam",
    "gui_app"
]

# Arquivos Python a incluir explicitamente
python_files = [
    "launcher.py",
    "credential_prompt.py",
    "credentials_manager.py",
    "delete_spam_emails.py",
    "check_spam_count.py",
    "verificar_spam.py",
    "gui_app.py"
]

# Adicionar arquivos Python à lista de arquivos a incluir
for py_file in python_files:
    include_files.append(py_file)

# Opções de build
build_options = {
    "packages": packages,
    "includes": includes,
    "include_files": include_files,
    "build_exe": os.path.join(base_dir, "build", "exe.win-amd64-3.13"),
    "zip_include_packages": ["*"],
    "zip_exclude_packages": []
}

# Configuração do executável
executables = [
    Executable(
        script="launcher.py",
        base="Win32GUI",  # Sem console para aplicação GUI
        target_name="GerenciadorDeSpam.exe",
        icon=os.path.join("icones", "gerenciador_spam.ico"),
        shortcut_name="Gerenciador de Spam do Gmail",
        shortcut_dir="DesktopFolder"
    )
]

# Configuração do setup
setup(
    name="GerenciadorDeSpam",
    version="1.0.0",
    description="Gerenciador de Spam do Gmail",
    author="Matheus Souza",
    options={"build_exe": build_options},
    executables=executables
)

print("Compilação concluída!")
