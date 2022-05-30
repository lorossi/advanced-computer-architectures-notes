# Advanced Computer Architectures notes

This repository contains the notes for the Advanced Computer Architectures course, relative to the 2021/2022 class of Computer Science and Engineering held at Politecnico di Milano.

Feel free to send a PR if you find any mistake that you are willing to fix!

## Latex compilation notes

The compilation of this LaTeX document is slightly problematic due to the intensive use of the `tikz` library.

If you are using VScode with the [LaTeX Workshop extension](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop), and you have Python (3.6+) installed on your computer, you have nothing to worry about, as I have set up the environment to work regardless of the adversities.
Just keep in mind that the first compilation might take a while _(up to a minute)_ due to the needed rendering of all the figures.

Otherwise, keep reading.
Due to its _awesomely user friendly features_, the user must:

- Create an empty folder called `tikztemp` in the repository root to hold all the temporary files it generates (note that this folder is already in the repository)
- Have a `.tikzstyles` file holding, well, all the styles used by `tikz`
- Enable a special flag (`--shell-escape`) on the compiler
- Compile using `latexpdf`, as I have not tried anything else

Furthermore, _due to the cryptic and mysterious nature of the tikz figures format_, I have been using another program called [TikZiT](https://tikzit.github.io/) to help me draw figure without completely losing my mind.
Sadly, this program introduced even more annoyances, like the increased incompatibility of the `tikzstyles` file it generates with the default, _vanilla_, `tikz` library.
In order to to fix this, I have created a Python script `cleantikz.py` that will clean the aforementioned file to remove all the fields that `TikZit` adds.

**Shall you ever edit the `tikzstyle.tikzsyles` file, remember to call the script, or the document won't compile!**

Finally, remember that the first compilation, due to the externalization of the images, will take a while.
Don't panic!

## Questions

### The notes are not consistent with the lectures. Why?

I found the lectures quite messy, without a clear ordering or a well defined sequence of topics.
This is why many chapters and sections in my notes are out of order with respect to the slides.

### The document does not compile. Can you help me?

Have you checked the README?
Go back to the [section above](#latex-compilation-notes) and read it again.

If it still does not work, open an issue.

### You made a mistake! How can that be fixed?

If you noticed and you feel kind enough to do the work for me, clone the repo and send me a pull request.

If you aren't feeling it, send me a message via email or open a discussion on GitHub.

### The thing you wrote does not make any sense! Can you fix it?

Sometimes I forget how to write as English is not my primary languages and the sentences lose all meaning.
If you spot one, follow the same steps as [above](#you-made-a-mistake)

### Why are you doing this?

I have always liked having clean notes on the courses I take and I do enjoy this process a lot.
I figured out that if I was doing this for myself, I could as well share my work with everyone else.

I just hope that these notes will help someone!

## Licensing

These notes are distributed under Creative Commons 4.0 license.
