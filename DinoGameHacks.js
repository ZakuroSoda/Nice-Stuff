// All codes go into Console in Google Chrome.

// The following code will disable you dying and make you immune.

let placeHolder = Runner.prototype.gameOver; // Saves the gameOver function to the variable placeHolder.

Runner.prototype.gameOver = function emptyFunction() { // Sets the gameOver function to an empty function.
    console.log("hit");
};

// The following code will enable you dying so that you can end the game.

Runner.prototype.gameOver = placeHolder // Sets the gameOver function back to the original working function.

// The following code will change your speed. "x" is the args for the speed. Theoretical limit is 6000. Use negative numbers to reverse.

Runner.instance_.setSpeed(x)

// The following code will change your jump height. "x" is the args for the height.

Runner.instance_.tRex.setJumpVelocity(x)