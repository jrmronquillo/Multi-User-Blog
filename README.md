# Jerome\'s Multi-User Blog
---------------------------
This project is an exercise in Web applications and development. It deploys a multi-user blog that allows multiple users to login and post blog content. In addition, this blog gives users the ability to like, edit and/or delete content. Lastly, users can post,edit and delete comments on each post. A submitted URL that is publicly accessible for an example:

<http://hello-udacity2323232323.appspot.com/blog>

## Installation
---------------
* ### Running this code
1. Install Python - Download available at <https://www.python.org/downloads/>
2. Install the python version of the Google App Engine SDK - Download available at https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
3. Sign Up for a Google App Engine Account
4. Create a new project in the Google Developer Console with a unique name - Google Developer Console at <https://console.cloud.google.com>
5. This project uses jinja2 to provide templating features with the html pages. (See how steps 6 and 7 to see how it is configured)
6. The following is included in the main.py to setup the jinja environment:
    ` import jinja2 `
`template_dir = os.path.join(os.path.dirname(__file__), 'templates')`
`jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)`
7. Also to make jinja work the following is included in the app.yaml configuration file as described below:
* ### Jinja Configuration
1. The following configuration app.yaml was used in development and is included in the project files:
`application: hello-udacity2323232323`
`version: 1`
`runtime: python27`
`api_version: 1`
`threadsafe: yes`
`handlers:`
`- url: /favicon\.ico`
` static_files: favicon.ico`
` upload: favicon\.ico`
`- url: .*`
`  script: main.app`
`- url: /bootstrap`
`  static_dir: bootstrap`
`libraries:`
`- name: jinja2`
`  version: latest`

## Usage
---------
* **Developing Locally:**
1. Transfer project directory to local machine.
2. From the project execute the following command - 'dev_appserver.py' to run application on local machine.
3. Default access is at http://localhost:8080
4. Note: If you somehow created multiple projects, the port may be different (e.g. http:localhost:10080)

* Alternatively, on a mac, the project can be run from the GoogleAppEngineLauncher that is downloaded from <https://cloud.google.com/appengine/downloads>
**To run:**
1. Select the "+" at the bottom left
2. Designating the project directory and clicking "Create"
3. Highlighting the project and pressing the "Run" button on the top right corner of the GoogleAppEngineLauncher. Access blog as noted above.

* **Project Deployment:**
1. To deploy project, use the following command
`gcloud app deploy`
2. Alternatively from the GoogleAppEngineLauncher, press "Deploy" in the top right corner
3. Access will then be publicly available via URL (e.g. http://project-name.appspot.com/blog)

## License
-----------
A license was not chosen as this code base was designed as more of an exercise to showcase skills learned from the Udacity course.

