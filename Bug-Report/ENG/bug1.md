##1. Character freezes in animation.

**Type**: Bug

**Priority**: -

**Game**: Baldur’s Gate 3

**Version**: 4.1.1.4494476 from 20.01.2025

**OS/Platform**: Windows 11/Steam

**Component**: Animations/Movement

**Short description**: Characters remain in the climbing animation after simultaneously pushing off from the ladder. 

**Description**: If two characters interact with the ladder at the same time and, while the climbing animation is playing, push them with any object—a grenade, a pull spell, or a push spell—both characters will fall, but their state will not change, and they will remain in the climbing animation. Further interaction with them will not produce any results. Both characters will fall, but their status will not change, and they will remain in the climbing animation. Further interaction with them will not produce any results; both will remain “stuck” in one place and continue to “climb.” To fix this, you need to load the last save.

**Steps to reproduce**:
1. Enter the game and load the save file.
2. Have character A interacts with the ladder.
3. Have character B also started interacting with the ladder. 
4. Make sure both characters are on the ladder. 
5. Throw a grenade at them or repel them with a spell.
6. Observe the result.

**Expected result**: the character fell, the animation stopped, he got up and returned to normal. You can continue to interact with him as usual. 

**Actual result**: the character “freezes” in one animation and does not respond to interaction with him.

![Bug's picture](.screenshots/bug1.png)
