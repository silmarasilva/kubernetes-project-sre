resource "aws_route53_record" "route53_silale" {
  zone_id = "Z00892882FUUMIJ25W8YA" #ID da zona hospedada
  name    = "www.silale.tech-talent.cf"
  type    = "A"

  alias {
    name                   = "afdf78e8ae2854aa9b2c804fd7c2078e-71848447a2f05d71.elb.us-east-1.amazonaws.com" #DNS LoadBalancer
    zone_id                = "Z26RNL4JYFTOTI" #Zona hospedada
    evaluate_target_health = true
  }
}