# nba-player-comparison-tool
# COMS W3132 Individual Project

## Author
Hayden Flowers htf2103@columbia.edu

## Project Title
NBA Player Comparison

## Project Description
The NBA Player Comparison is a tool that allows a user to input a player's name, and retrieve statistical comparisons between the players. Some of the metrics that will be covered will be points per game, assists, rebounds, and as well advanced metrics such as player efficiency rating, and true shooting percentage (TS%). This NBA tool is for basketball fans (such as me) and analysts who want an easy platform to compare NBA stats between players. This tool will allow users to search for one or two players and retrieve their stats, offering insights into player performance and facilitating better analysis and discussion.
## Timeline

*To track progress on the project, we will use the following intermediate milestones for your overall project. Each milestone will be marked with a tag in the git repository, and we will check progress and provide feedback at key milestones.*

| Date               | Milestone                                                                                              | Deliverables                        | Git tag    |
|--------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------|------------|
| **July&nbsp;15**   | Submit project description                                                                             | README.md                           | proposal   |
| **July&nbsp;17**   | Update project scope/direction based on instructor/TA feedback                                         | README.md                           | approved   |
| **July&nbsp;22**   | Basic project structure with empty functions/classes (incomplete implementation), architecture diagram | Source code, comments, docs         | milestone1 |
| **August&nbsp;2**  | More or less complete implementation. The goal is to have something you can share with others.         | Source code, unit tests             | milestone2 |
| **August&nbsp;9**  | Complete implementation. Final touches (conclusion, documentation, testing, etc.)                      | Source code, Conclusion (README.md) | conclusion |

*The column Deliverables lists deliverable suggestions, but you can choose your own, depending on the type of your project.*

## Requirements, Features and User Stories
Feature: Search for One Player and Display Basic Stats

User Story: As a user, I want to search for a single NBA player and see their basic stats (points per game, assists per game, rebounds per game) to understand their performance.
Feature: Search for Two Players and Compare Basic Stats

User Story: As a user, I want to search for two NBA players and compare their basic stats side-by-side to analyze their relative performance.
Feature: Search for One Player and Display Advanced Stats

User Story: As a user, I want to search for a single NBA player and see their advanced stats (player efficiency rating, true shooting percentage) to gain deeper insights into their performance.
Feature: Search for Two Players and Compare Advanced Stats

User Story: As a user, I want to search for two NBA players and compare their advanced stats to evaluate their performance in more detail.

Required Hardware/Software:

Flask for web development
nba_api for retrieving NBA statistics
A GitHub repository for version control
Basic HTML/CSS/JS for front-end development

## Technical Specification
Libraries:
  Flask: For creating the web application and handling routing.
  nba_api: To fetch NBA player statistics from the API.
Technologies:
  HTML/CSS: For building the web pages and styling.
  JavaScript: For client-side interactions and dynamic updates.
Rationale:
  Flask provides a lightweight and easy-to-use framework for web development, while nba_api offers a robust source for retrieving NBA statistics. Using these technologies supports the goal of creating a functional and user-friendly comparison tool.

## System or Software Architecture Diagram
*Include a block-based diagram illustrating the architecture of your software or system. This should include major components, such as user interface elements, back-end services, and data storage, and show how they interact. Tools like Lucidchart, Draw.io, or even hand-drawn diagrams photographed and uploaded are acceptable. The purpose of the diagram is to help us understand the architecture of your solution. Diagram asthetics do not matter and will not be graded.*

## Development Methodology
GitHub Projects Board: Track progress on tasks and milestones.
GitHub Issues: Keep track of issues or problems.
Git Branches & Pull Requests: Separate branches for features and bug fixes, with pull requests for code reviews.
GitHub Actions: Set up automated testing pipelines if applicable.
GitHub Wiki: Document project details and notes.
Testing:

Manual Testing: Verify forms and data display manually.
Unit Testing: Use Flask testing capabilities to ensure routes and functionality work as expected.

## Potential Challenges and Roadblocks
Challenge: Integrating nba_api with Flask.
Solution: Use mock data to test integration and ensure the API's response is handled correctly.
Challenge: Designing a user-friendly interface.
Solution: Iterate on design with user feedback and testing.

## Additional Resources
*Include any additional resources, tutorials, or documentation that will be helpful for this project.*

## Conclusion and Future Work
The project aims to create a comprehensive tool for comparing NBA players based on various statistics. Future work could involve expanding the feature set to include historical data, player comparisons over time, or integration with other data sources. Additionally, improvements to the UI/UX and incorporating user feedback will enhance the overall experience.
