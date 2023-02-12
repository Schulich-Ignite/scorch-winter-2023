

## Level 1

Modify the Coder! blog so that:

- The posts now each take up 12 columns and include the current information, and additional information (can be made up) about:
  - The language the post is in
  - Some tags that are links
  - A summary of the first little bit of the post
  - An author name and image (can use [unsplash for picture(s)](https://unsplash.com))
- Add [mermaid JS](https://mermaid.js.org/) to a blog post (use below HTML as example)

```html
<pre class="mermaid">
graph TD
    E[User] & A[Model] & B[View] & C[Template] & D[database]
    A --Define schema--> D
    B --requests data--> A
    A --Responds with data-->B
    B --Inject data--> C
    C --Return Rendered page--> B
    E --Request content--> B
    B --Respond--> E
    B --Store data--> D
</pre>
```

It should look like this:

[![](https://mermaid.ink/img/pako:eNpNkL1uwzAMhF-F0NApfgEPBfw3dOiSpF3sDKx1jdXGsivRCIog717JTuJqIu_uIyFeVDtoqFQdHY8d7cvGUnhV_ebhDvREWf0aAqdY5vW7wTlWRb1HP55YELuy1iz8wR6Hhc4oSUp8GgvybYeek-SZbpPz4Dn8TPDiKXLRy1ZuCz8OVns6G-nugXxlX-wXWnmQxeIUMymTs7SF1XDQNPIRMXKDqzkyL6Z2sAIr_9x8XR3ValV3Mjg89pVqo3q4no0OR7vEWKMk_BGNSkOp2X03qrHXkJvGQKHSJkxQqbgJG8WTDLtf2977JVMaDvfvF_H6B-H8e_0?type=png)](https://mermaid.live/edit#pako:eNpNkL1uwzAMhF-F0NApfgEPBfw3dOiSpF3sDKx1jdXGsivRCIog717JTuJqIu_uIyFeVDtoqFQdHY8d7cvGUnhV_ebhDvREWf0aAqdY5vW7wTlWRb1HP55YELuy1iz8wR6Hhc4oSUp8GgvybYeek-SZbpPz4Dn8TPDiKXLRy1ZuCz8OVns6G-nugXxlX-wXWnmQxeIUMymTs7SF1XDQNPIRMXKDqzkyL6Z2sAIr_9x8XR3ValV3Mjg89pVqo3q4no0OR7vEWKMk_BGNSkOp2X03qrHXkJvGQKHSJkxQqbgJG8WTDLtf2977JVMaDvfvF_H6B-H8e_0)

You only have to put mermaid JS on one page (you can do them all if you want), just include a comment to specify which page you put it on!

## Level 2

Create a personal site using a template from ([HTML5Up](https://html5up.net/) or [Start Bootstrap](https://startbootstrap.com/?showVue=false&showAngular=false&showPro=false)):

- Write content about yourself including
  - Your name, and something interesting about yourself
  - Hobbies
  - Favourite media (movies, tv shows, video games, books etc.) as reviews with some type of filter
  - Links to some of your projects you've built during the course (just link the HTML pages)
- Implement something using **1 of the below**:
  - https://animejs.com/
  - https://www.chartjs.org/ ([Use CDN version](https://www.chartjs.org/docs/latest/getting-started/installation.html))
  - http://mattboldt.github.io/typed.js/
  - https://p5js.org/
  - If you have another in mind just ask your mentor!


## Level 3

Build a website that is a database for animals:

- You can use a template or build the site from scratch
- Create interactive hero background with [particle JS](https://marcbruederlin.github.io/particles.js/)
  - [z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index) will help with some issues you might run into
  - Also keep in mind bootstrap elements are **transparent** you will need to add `bg-light` or `bg-dark` to give them a background colour
- Use a WYSIWYG editor ([quill](https://quilljs.com/), [editorjs](https://editorjs.io/), etc.) mixed with an HTML form where people can generate an HTML page about an animal (quill will probably be harder)
  - Don't worry about images. You can hardcode those afterwards.
  - Create several pages
- Create an overview page where you can see all of the animal pages that has a search with [lunr js](https://lunrjs.com/)
