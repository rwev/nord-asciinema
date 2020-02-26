# nord-asciinema

[Nord](https://www.nordtheme.com/) terminal theme for the [asciinema player](https://github.com/asciinema/asciinema-player). 

See [demo](https://rwev.dev/vim-fzf-versatility-for-value.html).

## usage

Load [`asciinema-theme-nord.css`](/asciinema-theme-nord.css) onto the page along with base [`asciinema-player.css`](https://github.com/asciinema/asciinema-player/releases) styles:

```html
<link rel="stylesheet" type="text/css" href="/asciinema-player.css" />
<link rel="stylesheet" type="text/css" href="/asciinema-theme-nord.css" /> 
```

Then, specify `theme="nord"` attribute on `<asciinema-player>` element:

```html
 <asciinema-player src="/your.cast" theme="nord"></asciinema-player>
```
