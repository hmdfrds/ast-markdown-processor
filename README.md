# AST Markdown Processor

A simple Markdown-to-HTML processor build in Python to understand the fundamentals of parsing and abstract syntax trees.

## Core Concept
This project was built as a learning exercise to understand how language processors work. It avoid complex dependencies and regular expressions, instead focusing on a classic two-stage architecture:
1. Parsing: A hand-written, recursive-descent parser scans the input text and builds an Abstract Syntax Tree (AST) a structured model of the document.
2. Rendering: A simple renderer "walks " the generated AST and translates each node into its corresponding HTML tag. This separation of concerns makes the processor robust and easy to extend.

## Features
Currently only supports a core subset of Markdown syntax:
- Headings (#, ##, etc.)
- Paragraphs (including multi-line)
- Bold (**text**)
- Italic (*text*)
- Nested bold and italic (**bold and *italic***)

