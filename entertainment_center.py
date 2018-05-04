#!/usr/bin/python
# -*- coding: latin-1 -*-

from movies import media
from movies import fresh_tomatoes

# Instantiate six movies
sw1 = media.Movie("Star Wars: Episode I - The Phantom Menace",
                  "Two Jedi Knights escape a hostile blockade to find allies and come across a young boy who may bring "
                  "balance to the Force, but the long dormant Sith resurface to claim their old glory.",
                  "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                  "https://www.youtube.com/watch?v=bD7bpG-zDJQ")
sw2 = media.Movie("Star Wars: Episode II - Attack of the Clones",
                  "Ten years after initially meeting, Anakin Skywalker shares a forbidden romance with Padmé Amidala, "
                  "while Obi-Wan investigates an assassination attempt on the senator and discovers a secret clone "
                  "army crafted for the Jedi.",
                  "https://images-na.ssl-images-amazon.com/images/I/51u4eDvof5L.jpg",
                  "https://www.youtube.com/watch?v=gYbW1F_c9eM")
sw3 = media.Movie("Star Wars: Episode III - Revenge of the Sith",
                  "Three years into the Clone Wars, the Jedi rescue Palpatine from Count Dooku. As Obi-Wan pursues a "
                  "new threat, Anakin acts as a double agent between the Jedi Council and Palpatine and is lured into "
                  "a sinister plan to rule the galaxy.",
                  "https://images-na.ssl-images-amazon.com/images/I/61ZDSUH2iiL._SL1001_.jpg",
                  "https://www.youtube.com/watch?v=5UnjrG_N8hU")
sw4 = media.Movie("Star Wars: Episode IV - A New Hope",
                  "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the "
                  "galaxy from the Empire's world-destroying battle-station while also attempting to rescue Princess "
                  "Leia from the evil Darth Vader.",
                  "http://www.impawards.com/1977/posters/star_wars_ver2.jpg",
                  "https://www.youtube.com/watch?v=1g3_CFmnU7k")
sw5 = media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                  "After the rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker "
                  "begins Jedi training with Yoda, while his friends are pursued by Darth Vader.",
                  "http://www.impawards.com/1980/posters/empire_strikes_back_ver1.jpg",
                  "https://www.youtube.com/watch?v=JNwNXF9Y6kY")
sw6 = media.Movie("Star Wars: Episode VI - Return of the Jedi",
                  "After a daring mission to rescue Han Solo from Jabba the Hutt, the rebels dispatch to Endor to "
                  "destroy a more powerful Death Star. Meanwhile, Luke struggles to help Vader back from the dark side "
                  "without falling into the Emperor's trap.",
                  "http://www.impawards.com/1983/posters/return_of_the_jedi_ver2.jpg",
                  "https://www.youtube.com/watch?v=5UfA_aKBGMc")

# Put them in a list
movies = [sw1, sw2, sw3, sw4, sw5, sw6]

# Open a webpage and display the six movies in a grid
fresh_tomatoes.open_movies_page(movies)