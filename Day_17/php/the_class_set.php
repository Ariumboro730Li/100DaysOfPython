<?php

class User {
    private $data = [];

    public function __set($name, $value)
    {
        $this->data[$name] = $value;
    }

    public function __get($name)
    {
        if (array_key_exists($name, $this->data)) {
            return $this->data[$name];
        }
        return null; // You can return any default value you prefer
    }

    public function save()
    {
        return $this->data;
    }
}

// using __set
$user = new User();
$user->name = 'John Doe';
$user->email = 'john@example.com';
$user->password = 'password';

// Accessing the properties using __get
echo $user->name . "\n";
echo $user->email . "\n";
echo $user->password . "\n";

$result = $user->save();

// Output the result as an array
print_r($result);
