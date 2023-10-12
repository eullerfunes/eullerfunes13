package br.com.euller.todolist.users;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping ("/users")


public class UserController {

    @PostMapping("/")
    public void creat(@RequestBody UserModel UserModel){
       System.out.println(UserModel.getUsername());
    }
}
