<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPLv3 License][license-shield]][license-url]

</div>

<h1 align="center">AutoPaper</h1>
<p align="center">Paper-based file backups made easy</p>

## About the project

AutoPaper makes backing up your files on paper much easier. It is ideal for files like SSH/GPG/... keys and similar.
Each file is compressed, divided into chunks and encoded into QR codes ready to be printed.

To restore these backups, you just scan the QR codes into your computer, and AutoPaper takes care of putting their
chunks back together, uncompressing them and outputting the original files.

## Roadmap

- [ ] MVP
  - [ ] Define data format  
  - [ ] Creating backups
    - [ ] Encoding files into QR codes
    - [ ] Chunking
    - [ ] Compression
      - [ ] Check whether files need to be compressed
  - [ ] Restoring backups
    - [ ] Decoding QR codes
    - [ ] Combining chunks together
    - [ ] Decompression
- [ ] Metadata pages
    - [ ] Generating first (info) page
    - [ ] Generating envelope text
- [ ] Encryption
- [ ] GPG key handling
  - [ ] If the key is on a keyserver, remove unnecessary data
  - [ ] Add GPG key ID to backup metadata
- [ ] SSH key handling
  - [ ] Add SSH key ID to backup metadata


[contributors-shield]: https://img.shields.io/github/contributors/stepanse/autopaper.svg?style=for-the-badge
[contributors-url]: https://github.com/stepanse/autopaper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/stepanse/autopaper.svg?style=for-the-badge
[forks-url]: https://github.com/stepanse/autopaper/network/members
[stars-shield]: https://img.shields.io/github/stars/stepanse/autopaper.svg?style=for-the-badge
[stars-url]: https://github.com/stepanse/autopaper/stargazers
[issues-shield]: https://img.shields.io/github/issues/stepanse/autopaper.svg?style=for-the-badge
[issues-url]: https://github.com/stepanse/autopaper/issues
[license-shield]: https://img.shields.io/github/license/stepanse/autopaper.svg?style=for-the-badge
[license-url]: https://github.com/stepanse/autopaper/blob/master/LICENSE.md