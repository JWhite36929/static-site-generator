# Static Site Generator 

This project takes markdown files (.md) and converts the markdown notation into the equivalent html format. 

## Usage
Any static resources should be placed into the static folder. 
This includes images and css. 
The html template is in the root of the project.

To generate pages paste markdown files into the content folder. 
This should follow the structure of the site. 

## Example
```
content/blog/post/index.md 
content/blog/post2/index.md 
content/contact/index.md 
```

Then run the build.sh script to generate the static site from the new content. 
Once the content has been generated push the changes to Github. 
GitHub Pages will read the changes and automatically deploy the site to https://jwhite36929.github.io/static-site-generator/.

To host locally for debugging run the main.sh script instead. 


This project was created following alongside boot.dev's course. All current assets and page content came from the course author. Personally I have not read Tolkien yet.
