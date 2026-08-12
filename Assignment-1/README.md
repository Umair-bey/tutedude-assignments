# Linux Basics — Tutedude Assignment 1

This is Assignment 1 of the DevOps course by Tutedude.

This assignment covers basic Linux command-line operations such as file and directory management, viewing file contents, searching, compression, downloading files, file permissions, and environment variables.

---

# 🐧 Linux Command-Line Practical

## Topics Covered

- Creating and renaming files and directories
- Viewing file contents
- Searching for patterns using `grep`
- Zipping and unzipping files
- Downloading files using `wget`
- Changing file permissions
- Working with environment variables

---

# 📋 Assignment Tasks

## 1. Creating and Renaming Files/Directories

Create a directory named `test_dir`:

```bash
mkdir test_dir
````

Create an empty file inside `test_dir`:

```bash
touch test_dir/example.txt
```

Rename `example.txt` to `renamed_example.txt`:

```bash
mv test_dir/example.txt test_dir/renamed_example.txt
```

Verify the result:

```bash
ls test_dir
```

Expected output:

```text
renamed_example.txt
```

---

## 2. Viewing File Contents

Display the complete contents of `/etc/passwd`:

```bash
cat /etc/passwd
```

Display only the first 5 lines:

```bash
head -n 5 /etc/passwd
```

Display only the last 5 lines:

```bash
tail -n 5 /etc/passwd
```

---

## 3. Searching for Patterns

Find all lines containing the word `root`:

```bash
grep "root" /etc/passwd
```

---

## 4. Zipping and Unzipping

Compress `test_dir` into `test_dir.zip`:

```bash
zip -r test_dir.zip test_dir
```

Create the destination directory:

```bash
mkdir unzipped_dir
```

Extract the ZIP archive:

```bash
unzip test_dir.zip -d unzipped_dir
```

Verify the extracted files:

```bash
ls -R unzipped_dir
```

---

## 5. Downloading Files

Download a file using `wget`:

```bash
wget https://example.com/sample.txt
```

> Note: The example URL may not provide an actual downloadable `sample.txt` file. If a successful download is required, use the URL provided by the instructor.

---

## 6. Changing Permissions

Create a file named `secure.txt`:

```bash
touch secure.txt
```

Make the file read-only for everyone:

```bash
chmod 444 secure.txt
```

Verify the permissions:

```bash
ls -l secure.txt
```

Expected permission format:

```text
-r--r--r-- secure.txt
```

### Permission Breakdown

| User   | Permission |
| ------ | ---------- |
| Owner  | Read       |
| Group  | Read       |
| Others | Read       |

---

## 7. Working with Environment Variables

Set the environment variable:

```bash
export MY_VAR="Hello, Linux!"
```

Verify the variable:

```bash
echo "$MY_VAR"
```

Expected output:

```text
Hello, Linux!
```

---

# 🖥️ Assignment Screenshot

![Linux Command-Line Practical](./screenshots/linux-command-line.png)

---

# 📚 Command Summary

| Task                         | Command                                                |
| ---------------------------- | ------------------------------------------------------ |
| Create directory             | `mkdir test_dir`                                       |
| Create empty file            | `touch test_dir/example.txt`                           |
| Rename file                  | `mv test_dir/example.txt test_dir/renamed_example.txt` |
| Display file contents        | `cat /etc/passwd`                                      |
| Display first 5 lines        | `head -n 5 /etc/passwd`                                |
| Display last 5 lines         | `tail -n 5 /etc/passwd`                                |
| Search for root              | `grep "root" /etc/passwd`                              |
| Create ZIP file              | `zip -r test_dir.zip test_dir`                         |
| Create extraction directory  | `mkdir unzipped_dir`                                   |
| Unzip archive                | `unzip test_dir.zip -d unzipped_dir`                   |
| Download file                | `wget https://example.com/sample.txt`                  |
| Create secure file           | `touch secure.txt`                                     |
| Make file read-only          | `chmod 444 secure.txt`                                 |
| Set environment variable     | `export MY_VAR="Hello, Linux!"`                        |
| Display environment variable | `echo "$MY_VAR"`                                       |

---

# ✅ Assignment Status

**Completed**

**Course:** DevOps
**Assignment:** 1
**Topic:** Linux Basics
**Student:** Umair Khan

```
```
