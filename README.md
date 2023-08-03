<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kirillwolkow/XSS-Scanner">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">XSS Vulnerability Scanner</h3>

  <p align="center">
    Another XSS Vulnerability Scanner but for Django!
    <br />
    <a href="https://github.com/kirillwolkow/XSS-Scanner"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kirillwolkow/XSS-Scanner/issues">Report Bug</a>
    ·
    <a href="https://github.com/kirillwolkow/XSS-Scanner/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

There are already some XSS Scanners out there which do a pretty good job.

This project is not only for my learning process to understand better how XSS attacks work and how I can make my web applications more secure against it.

This is also an open source project for applications built with [Django](https://www.djangoproject.com/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [BeautifulSoup4][BeautifulSoup4-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

```sh
# clone the repo
git clone https://github.com/kirillwolkow/XSS-Scanner

# create and activate a virtual environment (example virtualenv)
virtualenv env_name
source env_name/bin/activate # for Linux/Mac users
.\env_name\Scripts\activate # for Windows users

# install dependencies
pip install -r requirements.txt

# pull docker image and run container
./setup.sh
```

### Prerequisites

For this project you'll need Docker and Python installed on your system.
* Docker -> Refer to [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
* Python -> Refer to [https://www.python.org/downloads/](https://www.python.org/downloads/)

<!-- USAGE EXAMPLES -->
## Usage

Wait till container is running and create the database for DVWA. After that login with the default user credentials:
- username: admin
- password: password

```sh
# run the scanner script
python xss_scanner.py
```

You will see an output if an attack was successful or not.

[![Code Output](/images/code.png)](/images/code.png)

You can update to login url, the url to scan and also the JavaScript which will be submitted.

```python
def __init__(self):
    self.login_url = "http://localhost/login.php"
    self.url_to_scan = "http://localhost/vulnerabilities/xss_r/"
    self.js_script = "<script>alert('XSS')</script>"
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Scan for multiple forms on an URL
- [ ] Add suggestions to improve security
- [ ] A Django application which replaces DVWA (similar to Juice Shop) in order to target Django specific vulnerabilities
    - [ ] Create Docker image and publish to Docker Hub
    - [ ] Add forms with various difficulty levels
- [ ] Add predefined kinds of attacks (DOM, Reflected, Stored)

See the [open issues](https://github.com/kirillwolkow/XSS-Scanner/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Kenny Wolf - [@kennyrogerwolf](https://twitter.com/kennyrogerwolf) - mail@kennywolf.dev

Project Link: [https://github.com/kirillwolkow/XSS-Scanner](https://github.com/kirillwolkow/XSS-Scanner)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS
## Acknowledgments

* []()
* []()
* []() 

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[BeautifulSoup4-shield]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[BeautifulSoup4-url]: https://beautiful-soup-4.readthedocs.io/en/latest/
[contributors-shield]: https://img.shields.io/github/contributors/kirillwolkow/XSS-Scanner.svg?style=for-the-badge
[contributors-url]: https://github.com/kirillwolkow/XSS-Scanner/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kirillwolkow/XSS-Scanner.svg?style=for-the-badge
[forks-url]: https://github.com/kirillwolkow/XSS-Scanner/network/members
[stars-shield]: https://img.shields.io/github/stars/kirillwolkow/XSS-Scanner.svg?style=for-the-badge
[stars-url]: https://github.com/kirillwolkow/XSS-Scanner/stargazers
[issues-shield]: https://img.shields.io/github/issues/kirillwolkow/XSS-Scanner.svg?style=for-the-badge
[issues-url]: https://github.com/kirillwolkow/XSS-Scanner/issues
[license-shield]: https://img.shields.io/github/license/kirillwolkow/XSS-Scanner.svg?style=for-the-badge
[license-url]: https://github.com/kirillwolkow/XSS-Scanner/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kennywolf-dev
[product-screenshot]: images/code.png
