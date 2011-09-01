Feature: Full Moon Warning
  In order to know when to load my gun with silver bullets
  As a Werewolf hunter
  I want to know when Werewolves will be on the prowl

    Scenario: When will the next full moon be after given date
      Given today is "2011-09-01"
      When I call next_full_moon with today's date
      Then the result should be "2011-09-12"
