<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** marcelpinheiro, api-python-flask, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url] -->

[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/marcelpinheiro/)



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/marcelpinheiro/api-python-flask">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">RESTful</h3>

  <p align="center">
    This project shows how to build a RESTful api with Python and Flask
    <br />
    <a href="https://github.com/marcelpinheiro/api-python-flask"><strong>Explore the docs »</strong></a>
    <br />
    <!-- <br />
    <a href="https://github.com/marcelpinheiro/api-python-flask">View Demo</a>
    ·
    <a href="https://github.com/marcelpinheiro/api-python-flask/issues">Report Bug</a>
    ·
    <a href="https://github.com/marcelpinheiro/api-python-flask/issues">Request Feature</a>
  </p>
</p> -->



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The project consists in sharing the data of an csv file using an api to accomplish this task.


### Built With

* python 3.9.1
* flask
* flask_restful
* pandas



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

<!-- ### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ``` -->

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/marcelpinheiro/api-python-flask.git
   ```
2. Install requirements.txt packages
   ```sh
   pip install -r requirements.txt
   ```
3. Install the [Postman app](https://www.postman.com/downloads/) to show the responses


<!-- USAGE EXAMPLES -->
## Usage

After the installation of packages, run the app.py in your terminal
```sh
python app.py
```

If everything goes fine, you should see something like that:

![flask](images\Screenshot_5.png)

### Postman
Open the Postman app, click in Environments and create a new one. In variable name, put anything you want and in initial_value  and current_value, put: http://127.0.0.1:5000

![flask](images\Screenshot_7.png)

And then click in Collection and create a new one.

![flask](images\Screenshot_1.png)

&nbsp;
### The api has four options to choose:

| Parameter           |  Description                                    |
| ------------------- | -------------------                             |
| general             |  Return all the data                            |
|  totalwin           |  Return the total win of given member           |
|  wageramount        |  Return the total wager amount of given member  |
|  wagernumber        |  Return the wager amount of given member        |



&nbsp;
### Optional parameters
| Parameter           |  Description                                    |
| ------------------- | -------------------                             |
|  month              |  Return the data filter by month                |
|  game_id            |  Return the data filter by game                 |


&nbsp;
### Example of use:

1 - Get all data
```sh
http://127.0.0.1:5000/general
```
2 - Get the total win of member_id 1002
```sh
http://127.0.0.1:5000/totalwin?member_id=1002
```
3 - Get the total win of member_id 1002 filter by month
```sh
http://127.0.0.1:5000/totalwin?member_id=1002&month=03
```
4 - Get the total win of member_id 1002 filter by month and game_id
```sh
http://127.0.0.1:5000/totalwin?member_id=1002&month=04&game_id=7596
```


<!-- CONTACT -->
## Contact

<p> Marcel Pinheiro - marcelpinheiro@gmail.com </p>
<p> Linkedin: https://www.linkedin.com/in/marcelpinheiro/ </p>
Project Link: https://github.com/marcelpinheiro/api-python-flask



