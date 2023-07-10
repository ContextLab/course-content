**⚠ Experimental LLM-enhanced tutorial ⚠**

This notebook includes Neuromatch's experimental [Chatify](https://github.com/ContextLab/chatify) 🤖 functionality. The Chatify notebook extension adds support for a large language model-based "coding tutor" to the materials. The tutor provides automatically generated text to help explain any code cell in this notebook.

Note that using Chatify may cause breaking changes and/or provide incorrect or misleading information. If you wish to proceed by installing and enabling the Chatify extension, you should run the next two code blocks (hidden by default). If you do *not* want to use this experimental version of the NeuroMatch materials, please use the [stable](https://compneuro.neuromatch.io/tutorials/intro.html) materials instead.

To use the Chatify helper, insert the `%%explain` magic command at the start of any code cell and then run it (shift + enter) to access an interface for receiving LLM-based assitance. You can then select a "level" of explanation from the dropdown menu, depending on how much help you'd like.  To disable Chatify and run the code block as usual, simply delete the `%%explain` command and re-run the cell.

In its default configuration for this alpha release, we've set up Chatify to use cached responses for each code block. This means you'll see the same response every time you ask for an explanation about a given code block, at a given level of explanation. If you have an [OpenAI API key](https://openai.com/blog/openai-api), you may be interested in using a more interactive version of Chatify. Instructions for enabling custom queries and support for notebooks beyond the Neuromatch tutorials may be found [here](https://github.com/ContextLab/chatify).

Thanks for giving Chatify a try! Love it? Hate it? Either way, we'd love to hear from you about your Chatify experience!  Please consider filling out our [brief survey](https://forms.gle/jNq85KVvNwj1JHZV9) to provide feedback and help us make Chatify more awesome!

**Run the next two cells to install and configure Chatify...**