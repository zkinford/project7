from panda3d.core import CollisionHandlerEvent
from direct.interval.LerpInterval import LerpFunc
from direct.particles.ParticleEffect import ParticleEffect
# Regex module import for string editing.
import re

# "class Player" wasn't made in lecture... just gonna assume it goes here
from direct.showbase.ShowBase import ShowBase
class Player(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
#################### end assumed code
        self.cntExplode = 0
        self.explodeIntervals = {}

        self.traverser = traverser

        self.handler = CollisionHandlerEvent()

        self.handler.addInPattern('into')
        self.accept('into', self.HandleInto)
    
        self.traverser.addCollider(currentMissile.collisionNode, self.handler)

        def HandleInto(self, entry):
            fromNode = entry.getFromNodePath().getName()
            print("fromNode: " + fromNode)
            intoNode = entry.getIntoNodePath().getName()
            print("intoNode: " + intoNode)

            intoPosition = Vec3(entry.getSurfacePoint(self.render))

            tempVar = fromNode.split('_')
            shooter = tempVar[0]
            tempVar = intoNode.split('_')
            tempVar = intoNode.split('_')
            victim = tempVar[0]

            pattern = r'[0-9]'
            strippedString = re.sub(pattern, '', victim)

            if (strippedString == "Drone"):
                print(shooter + ' is DONE.')
                Missile.Intervals[shooter].finish()
                print(victim, ' hit at ', intoPosition)
                self.DroneDestroy(victim, intoPosition)

            else:
                Missile.Intervals[shooter].finish()
        
        def DroneDestroy(self, hitID, hitPosition):
            # Unity also has a find method, yet it is very inefficient if used anywhere but at the beginning of the program.
            nodeID = self.render.find(hitID)
            nodeID.detachNode()

            # Start the explosion.
            self.explodeNode.setPos(hitPosition)
            self.Explode(hitPosition)

        def Explode(self, impactPoint):
            self.cntExplode += 1
            tag = 'particles-' + str(self.cntExplode)

            self.explodeIntervals[tag] = LerpFunc(self.ExplodeLight, fromData = 0, toData = 1, duration = 4.0, extraArgs = [impactPoint])
            self.explodeIntervals[tag].start()

        def ExplodeLight(self, t, explosionPosition):
            if t == 1.0 and self.explodeEffect:
                self.explodeEffect.disable()

            elif t == 0:
                self.explodeEffect.start(self.explodeNode)

        def SetParticles(self):
            # "base" is underlinned, it is unknown as to why but is apparently fine
            base.enableParticles()
            self.explodeEffect = ParticleEffect()
            self.explodeEffect.loadConfig("./Assets/ParticleEffects/Explosions/basic_xpld_efx.ptf")
            self.explodeEffect.setScale(20)
            self.explodeNode = self.render.attachNewNode('ExplosionEffects')