# CLI arguments

## --encrypt, -e

Boolean optional value (defaults to False)

Controls whether to encrypt the files before backing them up

## --encrypt_pwd, -p

String optional value (defaults to \"\")

Sets password for encryption of the backup.
If `--encrypt` is True and `--encrypt-pwd` is not set, we'll ask for the password interactively.

## --force_compress, -c

Boolean optional value (defaults to False)

If True, we always compress all files.
If False, we check whether files are reasonable to compress before compressing them.