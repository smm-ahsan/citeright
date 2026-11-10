# CiteRight

A tiny command-line tool that formats academic references for books and journal articles in APA or MLA style.

## The four formats

Author input is always given as `Surname, Full Names`. Asterisks (`*...*`) mark text that would be italic in a formatted document; they are used so the italics stay visible in plain text.

**APA, book**

```
Surname, I. I. (Year). Title in sentence case. Publisher.
```

**APA, article**

```
Surname, I. I. (Year). Title in sentence case. *Journal Name*.
```

**MLA, book**

```
Surname, Firstname. Title in Title Case. Publisher, Year.
```

**MLA, article**

```
Surname, Firstname. "Title in Title Case." *Journal Name*, Year.
```

Title handling: APA uses sentence case (only the first word and the first word after a colon are capitalised - an approximation, so proper nouns inside a title come out lowercase). MLA uses Title Case, where small words such as "the", "and" and "of" stay lowercase unless they start the title.

## A note on accuracy

CiteRight covers the common book and journal-article cases in APA and MLA style. It does not cover edited volumes, chapters, websites, DOIs, multiple authors or page ranges. Citation rules also vary slightly between editions and institutions, so students should always double-check the output against their own institution's style guide before submitting work.

## Requirements

- Python 3
- Standard library only - nothing to install

## Usage

APA book:

```bash
python3 citeright.py --style apa --kind book --author "Anwar, Muhammad Ahsan" --year 2024 --title "Social Media and Small Business" --publisher "Island Press"
```

APA article:

```bash
python3 citeright.py --style apa --kind article --author "Anwar, Muhammad Ahsan" --year 2024 --title "Social Media and Small Business" --source "Malta Business Journal"
```

MLA book:

```bash
python3 citeright.py --style mla --kind book --author "Anwar, Muhammad Ahsan" --year 2024 --title "Social Media and Small Business" --publisher "Island Press"
```

MLA article:

```bash
python3 citeright.py --style mla --kind article --author "Anwar, Muhammad Ahsan" --year 2024 --title "Social Media and Small Business" --source "Malta Business Journal"
```

See `examples.md` for real captured output from these commands.

Rules the tool enforces: articles require `--source` and books require `--publisher`; a missing one exits with an error naming the argument. `--author` must contain a comma, as in "Surname, Full Names".

## License

MIT - see `LICENSE`.
