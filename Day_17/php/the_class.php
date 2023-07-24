<?php 

class User {
    public int $user_id;

    public function __construct()
    {
        var_dump($this->user_id);
    }
}

$my_user = new User;
$my_user->user_id = 1;

echo ($my_user->user_id);
