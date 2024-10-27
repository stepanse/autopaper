import argparse
import pathlib
from dataclasses import dataclass
from typing import List, Union, Optional

@dataclass
class Env:
    dest: pathlib.Path
    """destination to store backup or source from which to restore"""
    mode: str
    """backup or restore"""
    force_compress: bool
    """always compress all files"""
    encrypt: bool
    """encrypt files before backing them up"""
    password: str
    """encryption password"""
    source: Optional[Union[pathlib.Path, List[pathlib.Path]]]
    """files to be backed up"""

@dataclass
class FileToBackup:
    format_ver: int
    """Metadata format version"""
    filename: str
    """Original filepath"""
    checksum: str
    """File SHA256 checksum digest"""
    content: str
    """base-85 encoded file content"""
    compression_algo: Optional[str]
    """Compression algorithm used to compress the file"""
    encrypted: bool
    """Whether the file was encrypted"""
    chunk: Optional[int]
    "If not None, number of chunk stored in this code"
    chunks_total: Optional[int]
    """Number of total chunks needed to put together file"""

parser = argparse.ArgumentParser(
    description="paper-based file backups made easy",
    epilog="see https://stepanse.github.io/autopaper for docs"
)
parser.add_argument("-c", "--force_compress", action="store_true", help="always compress all files, do not use logic to check whether it actually makes sense")
parser.add_argument("-e", "--encrypt", action="store_true", help="encrypt files before creating backup")
parser.add_argument("-p", "--encrypt_password", dest="password", help="password for encryption, if --encrypt is True and --encrypt_password is not passed, it will be requested interactively")
parser.add_argument("-s", "--source", dest="file", help="source file(s) or folder(s) to be backed up")
parser.add_argument("mode", choices=["backup", "restore"], default="backup", help="create a new {backup} or {restore} from an existing one")
parser.add_argument("dest", help="destination to store backup or source from which to restore")

args = parser.parse_args()
env = Env(args.dest, args.mode, args.force_compress, args.password, args.password, source=args.file)
