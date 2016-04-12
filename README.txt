The NGTB Game 

#Development Information

	The game is being written in Python, using the PyGame API.
http://www.pygame.org/docs/

The project is saved through GitHub. This allows to people to work on the same file simultaneously without worry of losing work. Committing messages is necessary in order to record what’s been done. 

As of right now, the current version of NGTB Game is 1.6.2, which is currently being edited, so no safe execute is guaranteed. The first few versions have been declared unstable due to a directory redesign. Due to this oversight, versions will be released will a directory change that will access files in a version folder from now on. For example, Vx.x will still be located in Python Files directory, but will access folders from a directory that it was designed with, which should remain untouched. 

If changes have been made outside of code, i.e. sprite images and/or text files, the code may fail despite a stable version being used. 

If a change is needed to be checked outside of the code, using a stable version is highly recommended. 

Any code written should be in the main version .py file, unless it is a class definition (such as sprites) or functions that don't require global variables and don't return 2 or more items, in which class created a new .py file would be best.


#Goal for the game

	Very few design aspects of the game have been created so far. Most of the work done has been for the engine to run, which will be specific for this game. 

	The “big picture” is to have a top down rpg, where the player must go around collecting various pieces of new technology (i.e. 3D printing, VR) in different buildings around the GU campus and bring them back to NGTB. They must learn more about this technology online in order to discover its location. This should make people more aware of these technologies, NGTB, along with its location on campus. 

	Not every building around campus will be included, just the really big ones, and very little of the insides will be included. There is blueprints on the campus buildings around campus on the website. 

	Eventually the Map needs to start being designed according to a design of Pixel-Art. The style and resolution of Pixel-Art needs to be chosen. As of right now, something like StarDew Valley should suffice.

	The resolution of the game window is 800x600. The base resolution of images is 200x150, and scaled using pygame. This probably isn't the most efficient way to do this and will need to be re-thought.

 


