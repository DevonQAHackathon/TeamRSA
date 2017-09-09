# TeamRSA
Repository of the web application and api automation test framework of TeamRSA

WeatherApiTestFramework

Sample Web Application along with the test framework to automate testing

Application under test: The goal of this application is to suggest the user about the present diffence in temerature between the location he/she is travelling and currency conversion rate.

To Test the given application we have built our own Test automation framework using python. This framework is build for generic puropse which can be used to test any given API/Web automation.

Framework Requirment: Python 3.4 Nose 1.3.7 Selenium 3.5

We are utlizing the capability of nose test to do modular programing. Test cases and Test Data are stored in orginization format.

![Automation FrameWork](https://github.com/DevonQAHackathon/TeamRSA/blob/master/Images/image.png?raw=true?raw=true "Block Diagram")

Advantages of using the given Moduler Automation FrameWork:
- Well designed Folder Structured for Clean code (Prinicples)
- Common BaseTest which is derived form python unittest
- Common logger for logging events
- Drivers for communication
- Utilities 
- Easy to create drivers for communicating with different databases like MongoDB, SQL, MYSQL, SqlLite
- Easy to use for Performance Testing - Most Scalable
- Easy to use for Web UI automation
- Easy to use for API automation
- Reusable across Windows, Mac and Linux OS




Best Practices and Standards
Here are some best practices and conventions

- Separate out the concerns into different layers
- One class per module
- No multiple inheritance 
- Mixins to provide stateless behaviors and to be used as helper classes and not inherited
- Restrict inheritance to the same layer and do so only to model the problem and never for reuse of functionality
- Maintain composition between classification layers; Do not breach layer boundaries. (Ex: Product Libraries has 'drivers' than inheriting from drivers). In case a test needs direct access to lower layer functionality, use the 'Utilities' layering to achieve that.
