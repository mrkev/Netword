Netword 0.1
=======

An experimental Python interpreter of NetSpeak.

Note: This script is in very early development. Currently only connections are supported. More too come soon (hopefully. If homework and prelims allow).

##Usage

	$ python
	>> import Netword
	>> Netword.work_network("Hello.World.NetSpeak")

and you should get:

![Hello.World.NetSpeak](https://dl.dropboxusercontent.com/u/25751237/img/Screenshot%202013-10-01%2023.01.40.png)

##Supported NetSpeak

**Connections**

Usage:

	network = "Vee.Ajay.Prav.Vee"
    Netword.work_network(network)

draws

![a.b.c.a](https://dl.dropboxusercontent.com/u/25751237/img/Screenshot%202013-10-01%2022.26.15.png)

    network = "A.B.C.M.H.S.W.D.E.F.A.F.G.A.W.A.B.A.C.X.G.C.H.I.J.K.L.M"
    work_network(network)

![lollots](https://dl.dropboxusercontent.com/u/25751237/img/Screenshot%202013-10-01%2023.09.17.png)

*Note: sizes at the moment are meant to reflect node influence based on the number of connections they have*

##Unsupported NetSpeak

**Spaces**

Will allow writing several statements at once, and having separated networks.
   
    "A.B.C A.D A.E"

**Groups** 

Will allow distributed connections.

    "[A B C].D"


Groups are statements themselves, so connections can be declared inside them.

	"[A.B C].D"

**Node Properties**

Node properties will allow storage of data in node objects. The first string will be used as label, the first number as size, and the first hex string as color unless otherwise specified.

	"J('John Doe').F('Foo Bar', 23).H('Hello World', '#FF00EE').J"

**Edge Properties**

Edge properties will allow storage of data in edge objects. The first string will be used as label, the first number as magnitude, and hte first hex string as color for the edge. 

	"John.('Knows').Matt.('Works with').[Amanda Laura James]"

**Directionality** (If enabled)

Will allow edges with a direction to be drawn. Thus,

	"A.B"  !=  "B.A"

as A.B will be pointing from A -> B and B.A from B -> A. 

----------

I have no idea when these will be implemented, or in which order. I guess it all depends on my classes and clubs. If you'd like to contribue and keep this project moving forward at a faster pace, feel free to contact me though!

So what is NetSpeak?
----

A little descriptive language I thought would be cool to build. 

I'm in college. I'm taking a Networks class and I've come to realize how bloody difficult it is to represent networks in computers. I mean, you can't just type them. Usually, you have to open some software that wasn't designed to draw networks, and fiddle with the shapes and lines and text boxes. If you do have an application specialized in drawing diagrams the story isn't much different either. You still have to worry about the layout of shapes and manually add the connections.

NetSpeak is a little specification I put together of how I think I descriptive network language should look. It's still in the works. Netword is an attempt at a library that will prase and draw NetSpeak. 




