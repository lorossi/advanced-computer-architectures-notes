# Advanced Computer Architectures note

This repository contains the notes for the Advanced Computer Architectures course, relative to the 2021/2022 class of Computer Science and Engineering held at Politecnico di Milano.

Feel free to send a PR if you find any mistake that you are willing to fix!

## Latex compilation notes

The compilation of this LaTeX document is slightly problematic due to the intensive use of the `tikz` library.

If you are using VScode with the [LaTeX Workshop extension](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop), and you have Python (3.6+) installed on your computer, you have nothing to worry about, as I have set up the environment to work regardless of the adversities.
Just keep in mind that the first compilation might take a while (up to a minute) due to the needed rendering of all the figures.

Otherwise, keep reading.
Due to its *awesomely user friendly features*, the user must:

- Create an empty folder called `tikztemp` in the repository root to hold all the temporary files it generates
- Have a `.tikzstyles` file holding all the line and shapes styles used by it
- Enable a special flag (`-shell-escape`) on the `latexpdf` compiler

Furthermore, due to the cryptic and un usable nature of the tikz figures format, I have making use of another program called [TikZiT](https://tikzit.github.io/) to draw images in a faster way.

Sadly, this program introduced even more annoyances, like the increased incompatibility of the `tikz` styles file it generates with the default, *vanilla*, `tikz` library.
In order to to fix this, I have created a Python script `cleantikz.py` that will clean the aforementioned file to remove all the fields that `TikZit` adds.

Shall you ever edit the `tikzstyle.tikzsyles` file, remember to call it!

Finally, remember that the first compilation, due to the externalization of the images, will take a while.
Don't panic!

## Licensing

These notes are distributed under Creative Commons 4.0 license.
