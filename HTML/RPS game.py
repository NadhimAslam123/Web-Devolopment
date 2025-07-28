import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400,200))
pygame.display.set_captions("RPS")
White = (255,255,255)
Gray = (200,200,200)
Black = (0,0,0)
choices = ["Rock,Paper,Scissors"]
player_choice = ""
computer_choice = ""
result = ""
rock_button = pygame.Rect(50,200,100,40)
paper_button = pygame.Rect(200,200,100,40)
scissors_button = pygame.Rect(350,200,100,40)
def get_winner(player,computer):
    if player == computer:
        return "Draw"
    elif(player == "Rock" and computer == "Scissors")or\
        (player == "Scissors" and computer == "Paper")or\
        (player == "Paper" and computer == "Rock"):
        return "you win"
    else:
        return "You lose"