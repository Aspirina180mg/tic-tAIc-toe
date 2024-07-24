<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Aspirina180mg/tic-tAIc-toe">
    <img src="IMG/logo.png" alt="Logo" width="150" height="150">
  </a>

<h3 align="center">tic-tAIc-toe</h3>

<p align="center">
    Tic-Tac-Toe game with AI learning, it begins playing randomly, but after some rounds, it learns the playing style of the user and counter plays accoringly, it also has a global learning, with wich it learns from all the user instances.
    <br />
    <a href="https://github.com/aspirina180mg/tic-tAIc-toe"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/aspirina180mg/tic-tAIc-toe">View Demo</a>
    ·
    <a href="https://github.com/aspirina180mg/tic-tAIc-toe/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/aspirina180mg/tic-tAIc-toe/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![tic-tAIc-toe Screen Shot][product-screenshot]](https://example.com)

Tic-Tac-Toe game with AI learning, it begins playing randomly, but after some rounds, it learns the playing style of the user and counter plays accoringly, it also has a global learning, with wich it learns from all the user instances.

the game is made in Python, and distributed via APK file to be played in Android Devices. A web based client may be done, but not sure.

The player can choose to play against local or global AI:

* Local AI: a local dictionary stores the learning from the user, every time a play session is finished, this being the user winning or losing, the dictionary is updated.
* Global AI: a remote dictionary is stored in an API that is called when a player wants to play aginst the Global AI, at install, the client loads the global dictionary so offline play can be archieved, while a session is played, the local dictionary is sent to the API to update the global dictionary, if an error occurs, this action is canceled, if the action is successful, the global dictionary will be updated accounting for the new local info, when the play session ends, it will update the local dictionary instead of the global one.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
* [![Kivy][Kivy.org]][Kivy-url]
* [![AI (?)][AI.com]][AI-url]
* [![FastAPI][fastapi.tiangolo.com]][Fastapi-url]
* [![Render][render.com]][Render-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Work in progress...

<!--This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.-->


### Prerequisites

Work in progress...

<!--This is an example of how to list things you need to use the software and how to install them.

* npm
  ```sh
  npm install npm@latest -g
  ```-->

### Installation

Work in progress...

<!--1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/Aspirina180mg/tic-tAIc-toe.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage


Work in progress...

<!--Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] API Creation

  - [ ] creation of first global q_table
  - [ ] initialization of local q_table
  - [ ] download of global dictionary
  - [ ] update of global dictionary with local data
- [ ] Game creation

  - [ ] working win and lose state
  - [ ] creation of simple UI and assets
  - [ ] working simple user interaction, random gameplay, no AI
  - [ ] working game with dictionary implementation (select local or global gameplay)
  - [ ] working q-learning algorithm, updating local dictionary after every session
- [ ] Integration

  - [ ] integration with API, allowing for global gameplay with update
  - [ ] creation of final UI and assets, preffered dark mode, light mode maybe implemented.

See the [open issues](https://github.com/aspirina180mg/tic-tAIc-toe/issues) for a full list of proposed features (and known issues).

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

Misael García Torres [LinkedIN](https://www.linkedin.com/in/mgarciat/)- misagtor@gmail.com

Project Link: [https://github.com/Aspirina180mg/tic-tAIc-toe](https://github.com/Aspirina180mg/tic-tAIc-toe)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Aspirina180mg/tic-tAIc-toe.svg?style=for-the-badge
[contributors-url]: https://github.com/Aspirina180mg/tic-tAIc-toe/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Aspirina180mg/tic-tAIc-toe.svg?style=for-the-badge
[forks-url]: https://github.com/Aspirina180mg/tic-tAIc-toe/network/members
[stars-shield]: https://img.shields.io/github/stars/Aspirina180mg/tic-tAIc-toe.svg?style=for-the-badge
[stars-url]: https://github.com/Aspirina180mg/tic-tAIc-toe/stargazers
[issues-shield]: https://img.shields.io/github/issues/Aspirina180mg/tic-tAIc-toe.svg?style=for-the-badge
[issues-url]: https://github.com/Aspirina180mg/tic-tAIc-toe/issues
[license-shield]: https://img.shields.io/github/license/Aspirina180mg/tic-tAIc-toe.svg?style=for-the-badge
[license-url]: https://github.com/Aspirina180mg/tic-tAIc-toe/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mgarciat

[product-screenshot]: IMG/screenshot.png

[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://https://www.python.org/
[Kivy.org]: https://img.shields.io/badge/Kivy-333?style=for-the-badge&logo=kivy&logoColor=white
[kivy-url]: https://kivy.org/
[AI.com]: https://img.shields.io/badge/AI-00BFFF?style=for-the-badge&logo=ai&logoColor=white
[AI-url]: https://www.google.com/
[Fastapi.tiangolo.com]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[Fastapi-url]: https://fastapi.tiangolo.com/
[Render.com]: https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white
[Render-url]: https://render.com/