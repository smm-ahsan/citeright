#!/usr/bin/env python3
"""CiteRight - format academic references in APA or MLA style.

Covers the common book and journal-article cases. Standard library only.
"""

import argparse
import sys

SMALL_WORDS = {"a", "an", "the", "and", "or", "of", "in", "on", "at", "to", "for"}


def parse_author(author):
    """Split 'Surname, Full Names' into (surname, initials, first_name)."""
    if "," not in author:
        raise ValueError("--author must be in the format 'Surname, Full Names'")
    surname, _, full = author.partition(",")
    surname = surname.strip()
    full = full.strip()
    if not surname or not full:
        raise ValueError("--author must be in the format 'Surname, Full Names'")
    words = full.split()
    initials = " ".join(word[0].upper() + "." for word in words)
    first_name = words[0]
    return surname, initials, first_name


def sentence_case(title):
    """Approximation of sentence case.

    Lowercase every character, then uppercase the first character and the
    first character after a ': ' (subtitle start). Proper nouns inside the
    title are lowercased too - this is a documented approximation.
    """
    result = title.lower()
    if result:
        result = result[0].upper() + result[1:]
    idx = result.find(": ")
    if idx != -1 and idx + 2 < len(result):
        pos = idx + 2
        result = result[:pos] + result[pos].upper() + result[pos + 1:]
    return result


def title_case(title):
    """Capitalise each word, except small words stay lowercase mid-title."""
    words = title.split()
    out = []
    for i, word in enumerate(words):
        if i > 0 and word.lower() in SMALL_WORDS:
            out.append(word.lower())
        elif word:
            out.append(word[0].upper() + word[1:])
        else:
            out.append(word)
    return " ".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Format an academic reference in APA or MLA style."
    )
    parser.add_argument("--style", choices=["apa", "mla"], required=True,
                        help="Citation style to use.")
    parser.add_argument("--kind", choices=["book", "article"], required=True,
                        help="Type of source being cited.")
    parser.add_argument("--author", required=True,
                        help='Author as "Surname, Full Names", e.g. "Anwar, Muhammad Ahsan".')
    parser.add_argument("--year", required=True, help="Year of publication.")
    parser.add_argument("--title", required=True, help="Title of the book or article.")
    parser.add_argument("--source", help="Journal name (required for articles).")
    parser.add_argument("--publisher", help="Publisher name (required for books).")
    args = parser.parse_args(argv)

    if args.kind == "article" and not args.source:
        parser.error("--source is required for articles")
    if args.kind == "book" and not args.publisher:
        parser.error("--publisher is required for books")

    try:
        surname, initials, first_name = parse_author(args.author)
    except ValueError as exc:
        parser.error(str(exc))

    year = str(args.year)

    if args.style == "apa":
        title = sentence_case(args.title)
        if args.kind == "book":
            line = f"{surname}, {initials} ({year}). {title}. {args.publisher}."
        else:
            line = f"{surname}, {initials} ({year}). {title}. *{args.source}*."
    else:  # mla
        title = title_case(args.title)
        if args.kind == "book":
            line = f"{surname}, {first_name}. {title}. {args.publisher}, {year}."
        else:
            line = f'{surname}, {first_name}. "{title}." *{args.source}*, {year}.'

    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
