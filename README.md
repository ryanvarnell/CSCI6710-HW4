# The Clothing Carousel

<img id="mobile-site-image" src="source/images/site-image-mobile.png" alt="Mobile view of website.">

This was our group's final project for **CSCI 4710/6710 - Web Applications**. The idea of this website was to have a place
where users could build outfits using a carousel-style selection interface for individual pieces of clothing, giving
them a better idea of how all the pieces would work together.

## Tech Stack

<div id="tech-stack">
    <a href="https://getbootstrap.com/"><img src="source/images/bootstrap-logo.png" alt="Bootstrap" height="50"></a>
    <a href="https://jquery.com/"><img src="source/images/jquery-logo.png" alt="JQuery" height="50"></a> 
    <a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-262/"><img src="source/images/javascript-logo.png" alt="JavaScript" height="50"></a>
    <a href="https://www.w3.org/TR/CSS/#css"><img src="source/images/css-logo.png" alt="CSS3" height="50"></a>
    <a href="https://html.spec.whatwg.org/multipage/"><img src="source/images/html-logo.png" alt="HTML5" height="50"></a>
    <a href="https://flask.palletsprojects.com/en/2.3.x/"><img src="source/images/flask-logo.png" alt="Flask" height="50"></a> 
    <a href="https://www.python.org/"><img src="source/images/python-logo.png" alt="Python" height="50"></a> 
    <a href="https://www.sqlite.org/index.html"><img src="source/images/sqlite-logo.png" alt="SQLite" height="50"></a>
</div>

## Team

<section id="profiles">
<div class="profile">
    <div class="image-container">
        <a href="https://www.linkedin.com/in/ev-brown-cs-it/">
            <img src="static/img/about/about_page_evan.png" alt="Evan Brown">
        </a>
    </div>
    <div class="name-container">
        <p class="name"><a href="https://www.linkedin.com/in/ev-brown-cs-it/">Evan Brown</a></p>
    </div>
    <div class="email-container">
        <p class="email"><a href="mailto:evbrown1200@gmail.com">evbrown1200@gmail.com</a></p>
    </div>
</div>

<div class="profile">
    <div class="image-container">
        <a href="https://www.linkedin.com/in/ryanvarnell/">
            <img src="static/img/about/about_page_ryan.png" alt="Ryan Varnell">
        </a>
    </div>
    <div class="name-container">
        <p class="name"><a href="https://www.linkedin.com/in/ryanvarnell/">Ryan Varnell</a></p>
    </div>
    <div class="email-container">
        <p class="email"><a href="mailto:mail@ryanvarnell.com">mail@ryanvarnell.com</a></p>
    </div>
</div>

<div class="profile">
    <div class="image-container">
        <a href="https://www.linkedin.com/in/cris-zbavitel/">
            <img src="static/img/about/about_page_cris.jpg" alt="Cris Zbavitel">
        </a>
    </div>
    <div class="name-container">
        <p class="name"><a href="https://www.linkedin.com/in/cris-zbavitel/">Cris Zbavitel</a></p>
    </div>
    <div class="email-container">
        <p class="email"><a href="mailto:criszbav@gmail.com">criszbav@gmail.com</a></p>
    </div>
</div>
</section>

<img id="site-image" src="source/images/site-image.png" alt="Website in a desktop web browser.">

<style>
    #tech-stack a {
        padding: 5px;
        margin: auto;
        text-align: center;
    }

    #profiles {
        width: 65%;
        float: left;
        align-items: center;
    }

    .profile {
        display: inline-flex;
        flex-direction: column;
        width: 32%;
        min-width: 160px;
        align-items: center;
        justify-content: center;
    }

    .profile img {
        height: 120px;
        width: 120px;
        object-fit: cover;
        border-radius: 50%;
    }

    .profile .name-container {
        font-size: 25px;
        font-weight: bold;;
        margin-top: -10px;
    }

    .profile .email-container {
        margin-top: -30px;
    }

    #mobile-site-image {
        width: 35%;
        float: right;
        display: inline-block;
    }

    #site-image {
        align-self: center;
        margin-left: auto;
        margin-right: auto;
    }
</style>