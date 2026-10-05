import html

from docutils import nodes
from docutils.parsers.rst import (
    Directive,
    directives,
)


class CardSimpleDirective(Directive):
    """
     generates

     ```html
     <div style="
     border:1px solid #ddd;
     border-radius:8px;
     padding:15px;
    ">

       <div style="
          display:flex;
          gap:15px;
          align-items:flex-start;
       ">

          <img src="_static/img/item.png"
                style="width:120px; height:auto;">

          <div>
                <h3>Title.</h3>
                <p>asdsada</p>
          </div>

       </div>

       <div style="margin-top:15px;">
          <a href="https://example.com"
             class="sd-btn sd-btn-primary"
             style="display:block; text-align:center;">
                Read More
          </a>
       </div>

    </div>
    ```

     .. sourcecode:: rst
         .. card_simple::
            :title: Card name
            :image: _static/img/item.png
            :description: description example
            :button_url: https://example.com
            :button_text: Read More
    """

    required_arguments = 0
    optional_arguments = 5
    final_argument_whitespace = False

    option_spec = {
        "title": directives.unchanged,
        "image": directives.unchanged,
        "description": directives.unchanged,
        "button_url": directives.unchanged,
        "button_text": directives.unchanged,
    }

    def run(self):
        title: str = self.options.get("title")

        image: str = self.options.get("image")
        description: str = self.options.get("description")
        button_url: str = self.options.get("button_url")
        button_text: str = self.options.get("button_text", "Read More")

        result = f"""
        <div style="
            border:1px solid #ddd;
            border-radius:8px;
            padding:15px;
        ">
    
            <div style="
                display:flex;
                gap:15px;
                align-items:flex-start;
            ">
    
                <img src="{image}"
                    style="width:120px; height:auto;">
    
                <div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
    
            </div>
    
            <div style="margin-top:15px;">
                <a href="{button_url}"
                    class="sd-btn sd-btn-primary"
                    style="display:block; text-align:center;">
                    {button_text}
                </a>
            </div>
    
        </div>
        """

        return [nodes.raw("", result, format="html")]


def setup(app):
    app.add_directive("card_simple", CardSimpleDirective)
