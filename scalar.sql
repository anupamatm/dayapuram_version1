

product = Product.objects.get(id=1)
select * from Product where id=1

product=product.objects.filter(vendor = 'Adidas')
select * from product where vendor = 'Adidas'



seller = Reseller.objects.all()
select * from Reseller

data=Reseller.objects.values('title','img')
select title,img from Reseller 



products.objects.filter(id=pid).update(desc="sports shoe for mens",price=2999)
update products set desc="sports shoe for men",price=2999 where id=pid


Entry.objects.filter(pub_date__lte='2006-01-01') 
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';


Entry.objects.get(headline__exact="Man bites dog") 
SELECT * from blog_entry WHERE headline = 'Man bites dog'; 


 Blog.objects.get(name__iexact="beatles blog")
 Would match a Blog titled “Beatles Blog”, “beatles blog”, or even “BeAtlES blOG”.


 Entry.objects.get(headline__contains='Lennon') 
 SELECT * from blog_entry WHERE headline LIKE '%Lennon%'; 
--  Note this will match the headline 'Today Lennon honored' but not 'today lennon honored'.



Entry.objects.get(headline__startwith='L') 
 SELECT * from blog_entry WHERE headline LIKE 'L%'; 


Entry.objects.get(headline__endwith='L') 
 SELECT * from blog_entry WHERE headline LIKE '%L';


  q1.filter(pub_date__gte=datetime.date.today())
  select ... where pub_date >= CURRENT_DATE;

  




select * from reseller_app_product;
SELECT AVG(p_price) AS AvgMarks FROM reseller_app_product;
SELECT COUNT(p_price) FROM reseller_app_product;
SELECT FIRST(p_name) FROM reseller_app_product;



SELECT  p_name ( UPPER (first_name) ) as product_name FROM reseller_app_product;





SELECT    UPPER (p_name) as product_name FROM reseller_app_product;
SELECT    LOWER(p_name) as product_name FROM reseller_app_product;