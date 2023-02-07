

## Level 1

Modify the Coder! blog so that:

- The posts now each take up 12 columns and include the current information, and additional information (can be made up) about:
  - The language the post is in
  - Some tags that are links
  - A summary of the first little bit of the post
  - An author name and image (can use [unsplash for picture]())
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
