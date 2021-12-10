# ITWS 1100 Lab 9

## Description

In this lab we used a JSON file to hold all the required info for each lab, so that we could use some JS/jQuery to generate the page for us automatically, instead of having to write more HTML to add a new lab each time. This method makes a lot of sense, especially for website that add formatted content frequently (like news website articles, software website changelogs, blog posts, etc.). Overall this lab went somewhat smoothly for me. I had to spend some time troubleshooting why I couldn't properly access my JSON file, and then I wrote some code that didn't manipulate the imported JSON object correctly, so I also had to fix that. But once I got my AJAX function up and running, it was very easy to modify and add new content, and it will be super easy in the future, too. The only downside is that it could be a bit difficult to add more custom content in, like if I wanted to have a different design/layout for each lab. But I'm sure it's possible with some more knowledge.

## Files for grading

* `iit/projects/assets/labs_builder.js` - JS file that builds all the lab HTML
* `iit/projects/assets/labs.json` - JSON file that holds all the lab content
* `iit/projects/projects.html` - modified projects page

## Info

* GitHub ID: callumhauber
* Repo Name: ITWS-1100
* Discord: Callum#5049

## Sources

* <https://api.jquery.com/each/>
