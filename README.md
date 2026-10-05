# home_recipes
https://sphinx-design.readthedocs.io/en/latest/get_started.html
https://fontawesome.com/s

# Render locally

## Build local
```shell
rm -rf docs/build/html; sphinx-build -b html docs/source docs/build/html
```

## Web local
```shell
python3 -m http.server --directory docs/build/html
```

# Snippets

## Link static image

```rst
.. image::
   /_static/img/profile.png
   :target: /_static/img/profile.png
   :loading: lazy
   :alt: Profile
   :align: center
```