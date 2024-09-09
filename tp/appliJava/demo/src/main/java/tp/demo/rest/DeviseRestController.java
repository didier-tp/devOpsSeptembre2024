package tp.demo.rest;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController //Composant Spring de type controller de WS REST
@RequestMapping(value = "/devise" , headers="Accept=application/json")
public class DeviseRestController {

    @Autowired
    private ServiceDevise serviceDevise;

    @GetMapping("")
    public Devise getAllDevises(){
        return serviceDevise....;
    }


}
