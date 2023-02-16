You now know how to host websites, so let's host a few.

## Deliverables

To get full points you will need to do all 3 levels

### Level 1

Using ezcv create a personal site and host it through github pages

Also setup 1-3 more of the sites you've created so far and include links to them in the projects section of your site

### Level 2

Use variables in your pipeline:

- Set your workflow to manual dispatch
- Include a version number field
- Include a description field to describe your changes

Your first Job in the workflow should be to run the steps

```yaml
steps:
      - name: Print inputs
        run: echo Inputs are ${{ inputs.version_number }} ${{ inputs.description }} 
```

### Level 3 

Implement 2 actions from the workplace, some good options are:

- [Minify images](https://github.com/marketplace/actions/image-optimizer)
- [Minify HTML/CSS/JS](https://github.com/marketplace/actions/minify-css-js-and-html-files-in-github-action)
- [Automatically create a github relase](https://github.com/marketplace/actions/create-release)

## hints

- [inputs](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs)
- [run-name](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#run-name)
- [Manual running](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_dispatch)

## Resources

- [Code minifying](https://en.wikipedia.org/wiki/Minification_(programming))
- [Image minifying](https://www.net7.be/blog/article/image_minification.html)
