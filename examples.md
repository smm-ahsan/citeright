# CiteRight examples

Real output captured from actual runs of `citeright.py`.

## APA book

```bash
python3 citeright.py --style apa --kind book --author "Anwar, Muhammad Ahsan" --year 2024 --title "Social Media and Small Business" --publisher "Island Press"
```

```
Anwar, M. A. (2024). Social media and small business. Island Press.
```

## APA article

```bash
python3 citeright.py --style apa --kind article --author "Anwar, Muhammad Ahsan" --year 2024 --title "Social Media and Small Business" --source "Malta Business Journal"
```

```
Anwar, M. A. (2024). Social media and small business. *Malta Business Journal*.
```

## MLA book

```bash
python3 citeright.py --style mla --kind book --author "Anwar, Muhammad Ahsan" --year 2024 --title "Social Media and Small Business" --publisher "Island Press"
```

```
Anwar, Muhammad. Social Media and Small Business. Island Press, 2024.
```

## MLA article

```bash
python3 citeright.py --style mla --kind article --author "Anwar, Muhammad Ahsan" --year 2024 --title "Social Media and Small Business" --source "Malta Business Journal"
```

```
Anwar, Muhammad. "Social Media and Small Business." *Malta Business Journal*, 2024.
```

## The classic textbook example

```bash
python3 citeright.py --style apa --kind book --author "Smith, John" --year 2020 --title "The Art of Focus" --publisher "Acme Press"
python3 citeright.py --style mla --kind book --author "Smith, John" --year 2020 --title "The Art of Focus" --publisher "Acme Press"
```

```
Smith, J. (2020). The art of focus. Acme Press.
Smith, John. The Art of Focus. Acme Press, 2020.
```
