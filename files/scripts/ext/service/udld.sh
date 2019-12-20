#!/bin/bash

function udldServicePreStop()
{
    docker exec udld bash -c "date > /PreStop"
    docker exec udld bash -c "udldctl dyingGasp"
}


